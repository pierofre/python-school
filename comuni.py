import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
from pathlib import Path


class ComuniPop(object):

    def __init__(self):
        if Path("comuni_pop.pkl").is_file():
            self.comuni = pd.read_pickle("comuni_pop.pkl")
        else:
            self.comuni = self._make_dataframe()

    def _get_comuni(self):
        r = requests.get("https://it.wikipedia.org/wiki/Comuni_d'Italia_per_popolazione")
        r.encoding = "latin1"
        sp = BeautifulSoup(r.text, "html.parser")
        comuni = sp.find("table").find_all("tr")
        mx = []
        for row in comuni:
            cols = row.find_all("td")
            cols = [data.text.strip().replace("\xa0", "") for data in cols]
            mx.append(cols)

        del(mx[0])
        return mx

    def _save_dataframe(self):
        df = self.comuni.to_pickle("comuni_pop.pkl")

    def _make_dataframe(self):
        df = DataFrame(self._get_comuni(), columns=["id", "Comune", "Regione", "Provincia", "Abitanti"])
        print("Data retrieved succesfully. Here's a sample:\n")
        print(df.head(10))
        return df

if __name__ == "__main__":
    ComuniPop()._save_dataframe()
    print("\nFile `comuni_pop.pkl` creato con successo")
