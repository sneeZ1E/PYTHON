
#1. uzdevums
from asyncio import events


def pirmaisUzdevums(par1, par2):
    reizinajums = par1*par2
    summa = par1+par2
    if reizinajums<1000 :
        return reizinajums
    else:
        return summa

#print("The result is", pirmaisUzdevums(30, 30))

#2. uzdevums
def otraisUzdevums(): #def otraisUzdevums(sakums = 0, beigas = 10, solis = 1):
    esosais = 0
    ieprieksejais = 0
    for i in range(10):
        ieprieksejais = esosais
        esosais = i
        summa = ieprieksejais + esosais
        print("Current number", esosais, "Previous number", ieprieksejais, "Sum:", summa)
    return
#otraisUzdevums()

#3. uzdevums
def tresaisUzdevums(teksts):
    print("Sākotnējais teksts ir", teksts)
    print("Tikai pāra indeksa burti:")
    for i in range(0, len(teksts), 2):
        print(teksts[i])
    return

#tresaisUzdevums("pynative")

#4. uzdevums
def ceturtaisUzdevums(teksts, n):
    print("Teksts:", teksts)
    print("Noņemot pirmos", n, "burtus sanāk:", teksts[n:])
    return

#ceturtaisUzdevums("pynative", 4)

#5. uzdevums
def piektaisUzdevums(saraksts):
    print("Dotais saraksts:", saraksts)
    print("Result is", saraksts[0]==saraksts[-1])
    return

skaitli1 = [10, 20, 30, 40, 10]
skaitli2 = [75, 65, 35, 75, 30]

#piektaisUzdevums(skaitli2)


