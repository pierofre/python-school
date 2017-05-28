import learner

studente = learner.Learner("Alan", "Marazzi", 4,130)
with open ("studenti.txt", "a") as b:
    b.write("{}\t{}\t{}\t{}\t{}\n".format(studente.name, studente.surname, studente.level, studente.classes, studente.days))
