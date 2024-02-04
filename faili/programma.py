

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

def uzrakstit_vestuli(vards, uzvards, dzimums, vecums, index):
    if dzimums == "s":
        galotne1 = "a"
        galotne2 = "usi"
    else:
        galotne1 = "s"
        galotne2 = "is"

    fails = open("faili/vestules/vestule{}.txt".format(index), "w", encoding="utf-8")
    fails.write("Sveik{}, {} {}! \n".format(galotne1, vards, uzvards))
    fails.write("Jūs esat laimēj{} {}0 EUR!".format(galotne2, vecums)) 
    
    return

def apstradat_datus(dati):
    dati = dati.split()
    if dati[4] == "Sieviete":
        dzimums = "s"
    else:
        dzimums = "v"
    return [dati[0], dati[1], dati[3][:-1], dati[4][:-1], dzimums]

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


cilveki = nolasit("faili/cilveki.txt")
index = 1
for cilveks in cilveki:
    cilveka_dati = apstradat_datus(cilveks)
    uzrakstit_vestuli(cilveka_dati[0], cilveka_dati[1], cilveka_dati[2], cilveka_dati[3], index)
    index+=1
    


# izveidojas fails kur katra rindina ir vards, uzvards - vecums
# Anna Bērziņa - 23, sieviete
# Sveiks/-a, ....! Tu esi laimējis/-usi .... Euro!


# print(nolasit("faili/teksts.txt"))
# pierakstit("Yo\n\n", "faili/teksts.txt")