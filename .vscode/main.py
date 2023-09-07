


aboluCenaKg = 0.69 #abolu cena eiro kg
cukuraCenaKg = 1.35 #cukura cena eiro kg

aboluMinDaudzumsGramos = 1000 #mazakais iespejamais abolu daudzums
cukuraMinDaudzumsGramos = 333 #mazakais iespejamais cukura daudzums

print("Labdien!")

aboluDaudzums = float(input("Cik daudz ābolu tev ir gramos?")) #parbauda cik abolu ir lietotajam
    

if aboluDaudzums < aboluMinDaudzumsGramos:
    print("Šodien ievārījumu neēdīsi :(")

break

cukuraDaudzums = float(input("Cik daudz cukurs tev ir gramos?")) #parbauda cik daudz cukura ir lietotajam
    
if cukuraDaudzums < cukuraMinDaudzumsGramos:
    print("Šodien ievārījumu neēdīsi :(")

def aprekinat(aboluDaudzums, aboluCenaKg)
    return aboluDaudzums * aboluCenaKg
print("Āboli izmaksās", aprekinat(aboluDaudzums, aboluCenaKg))

