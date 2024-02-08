class cilveks:
    def __init__(self, vecums, dzimums, vards):
        self.age = vecums
        self.gender = dzimums
        self.name = vards
        self.money = 0

    def dzimsanas_diena(self):
        self.age += 1

    def mainit_vardu(self, jaunais_vards):
        self.name = jaunais_vards

    def aprakstit_sevi(self):
        if self.gender == "s":
            dz = "sieviete"
        elif self.gender == "v":
            dz = "vīrietis"
        else:
            dz = self.gender
        print("Mani sauc {}, man ir {} gadi. Esmu {}. Man ir {} Euro!".format(self.name, self.age, dz, self.money))

    def nopelnit(self, nopelnita_nauda):
        self.money += nopelnita_nauda

    def nomainit_dzimumu(self, jaunais_dzimums):
        self.gender = jaunais_dzimums
        
    def uztaisit_spam_vestuli(self, failu_mape):
        if self.gender == "s":
            sveiki_galotne = "a"
            laimests_galotne = "usi"
        elif self.gender == "v":
            sveiki_galotne = "s"
            laimests_galotne = "is"
        else:
            sveiki_galotne = "i"
            laimests_galotne = "is"

        faila_nosaukums = failu_mape + "spams" + self.name + str(self.age)
        faila_teksts = "Sveik{}, {}! Jūs esat laimēj{} {} EUR!".format(sveiki_galotne, self.name, laimests_galotne, self.age*35)
        with open(faila_nosaukums, "w", encoding="utf-8") as fails:
            fails.write(faila_teksts)
        self.nopelnit(self.age*35)
        self.aprakstit_sevi()



# persona1 = cilveks(32, "sieviete", "Marta")
# persona1.aprakstit_sevi()
# persona1.nopelnit(30)
# persona1.aprakstit_sevi()
# persona1.nomainit_dzimumu("v")
# persona1.aprakstit_sevi()
# persona1.uztaisit_spam_vestuli("objektu orienteta programmesana/spams/")

turpinat = "t"
cilveki = []
while turpinat == "t":
    vards = input("Ievadiet cilvēka vārdu!:")
    vecums = -1
    while vecums<0:
        vecums = int(input("Ievadiet cilvēka vecumu!:"))
    dzimums = input("Ievadiet cilvēka dzimumu (s/v) !:")
    cilveki.append( cilveks (vecums, dzimums, vards))
    turpinat = input("Ja vēlies pievienot vēl cilvēkus, raksti 't'!")

for viens in cilveki:
    viens.uztaisit_spam_vestuli("objektu orienteta programmesana/spams/")
