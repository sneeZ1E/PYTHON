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
        


persona1 = cilveks(32, "sieviete", "Marta")
persona1.aprakstit_sevi()
persona1.nopelnit(30)
persona1.aprakstit_sevi()
persona1.nomainit_dzimumu("v")
persona1.aprakstit_sevi()


#turpinat = "t"
#cilveki = []
#while turpinat == "t":
#    vards = input("Ievadiet cilvēka vārdu!:")
#    vecums = int(input("Ievadiet civlēka vecumu!:"))
#    dzimums = input("Ievadiet cilvēka dzimumu (s/v) !:")
#    cilveki.append( cilveks (vecums, dzimums, vecums))
#    turpinat = input("Ja vēlies pievienot vēl cilvēkus, raksti 't'!")

#for viens in cilveki:
#    print(viens.age)
