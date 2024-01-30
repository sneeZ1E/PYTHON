def ierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "w", encoding='utf-8')
    fails.write(teksts)
    fails.close()

def pierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "a", encoding='utf-8')
    fails.write(teksts)
    fails.close()

def nolasit(faila_nosaukums):
    with open(faila_nosaukums, "r", encoding='utf-8') as fails:
        rindas = fails.readlines()
    return rindas




vardi = ["Anna", "Maija", "Jānis", "Kaspars"]
uzvardi = ["Bērziņa", "Paija", "Ozols", "Kasprets"]
vecums = [23, 150, 89, 11]
dzimums = ["s", "s", "v", "v"]
statuss = ["Neprecējies", "Neprecējies", "Neprecējies", "Precējies"]

ierakstit("", "faili/cilveki.txt")
for i in range(len(vardi) ):
    if dzimums[i] == "s":
        rakstamais = "Sieviete"
    else:
        rakstamais = "Vīrietis"
    teksts = "{} {} - {}, {}, {} \n".format(vardi[i], uzvardi[i], vecums[i], rakstamais, statuss[i])
    pierakstit(teksts, "faili/cilveki.txt")

# izveidojas fails kur katra rindina ir vards, uzvards - vecums
# Anna Bērziņa - 23, sieviete



# print(nolasit("faili/teksts.txt"))
# pierakstit("Yo\n\n", "faili/teksts.txt")