def dienas_mekletajs (esosais_gads, esosais_menesis, esosais_datums, esosa_diena, dzimsanas_gads, dzimsanas_menesis, dzimsanas_datums):
    menesu_dienu_skaits = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dienu_nosaukumi = ["Nekas", "pirmdiena", "otrdiena", "trešdiena", "ceturtdiena", "piektdiena", "sestdiena", "svētdiena"]
    
    #Tiek skaitits cik dienas pagajusas
    #Tiek parbaudits vai sogad jau ir bijusi dzimsanas diena
    
    pagajusas_dienas = 0
    pagajusie_gadi = esosais_gads - dzimsanas_gads

    if vai_datums_jau_pagajis(esosais_menesis, esosais_datums, dzimsanas_menesis, dzimsanas_datums) == False:
        pagajusie_gadi = pagajusie_gadi-1

    pagajusas_dienas = pagajusie_gadi*365
    
    garie_gadi = 0

    parbaudes_gads_sakums = dzimsanas_gads
    if vai_datums_jau_pagajis(dzimsanas_menesis, dzimsanas_datums, 2, 29):
        parbaudes_gads_sakums = parbaudes_gads_sakums+1
    
    if vai_datums_jau_pagajis(esosais_menesis, esosais_datums, 2, 29) == False:
        parbaudes_gads_beigas = esosais_gads-1



    parbaudes_gads_beigas = esosais_gads

    for gads in range(parbaudes_gads_sakums, parbaudes_gads_beigas, 1):
        if gads % 4 == 0:
            garie_gadi = garie_gadi+1
        if gads % 100 == 0 and gads % 400 != 0:
            garie_gadi = garie_gadi-1

    pagajusas_dienas = pagajusas_dienas+garie_gadi

    #Tiek skaitits cik pilni menesi pagajusi kops pedejas dzd
    if esosais_menesis>=dzimsanas_menesis:
        pilni_menesi = esosais_menesis-dzimsanas_menesis

    else:
        pilni_menesi = esosais_menesis+12-dzimsanas_menesis

    if vai_datums_jau_pagajis(1, esosais_datums, 1, dzimsanas_datums) == False:
        pilni_menesi -= 1

    dienas_menesos = 0


    menesis = dzimsanas_menesis
    while menesis != esosais_menesis:
        dienas_menesos += menesu_dienu_skaits[menesis]
        menesis += 1
        if menesis == 13:
            menesis=1
    
    pagajusas_dienas += dienas_menesos

    #Tiek skaitits cik dienas pari pilniem menesiem ir pagajusas

    if esosais_datums>=dzimsanas_datums:
        ekstra_dienas = esosais_datums-dzimsanas_datums
    else:
        ekstra_dienas = esosais_datums + menesu_dienu_skaits[esosais_menesis-1] - dzimsanas_datums

    pagajusas_dienas += ekstra_dienas
    
    print("Kopš dzimšanas dienas ir pagājušas: ", pagajusas_dienas, "dienas.")
    
    dienu_atlikums = pagajusas_dienas %7
    dzimsanas_diena = esosa_diena-dienu_atlikums

    if dzimsanas_diena<=0:
        dzimsanas_diena +=7

    print("Jums ir ", pagajusie_gadi, " gadi, ", pilni_menesi, " mēneši un ", ekstra_dienas, "dienas.")

    return dienu_nosaukumi[dzimsanas_diena]


def vai_datums_jau_pagajis(esosais_menesis, esosais_datums, dzimsanas_menesis, dzimsanas_datums):
    if esosais_menesis>dzimsanas_menesis:
        return True
    if esosais_menesis<dzimsanas_menesis:
        return False
    if esosais_datums<dzimsanas_datums:
        return False
    return True



def ievades_datu_parbaude(dzimsanas_gads, dzimsanas_menesis, dzimsanas_datums, esosais_gads, esosais_menesis, esosais_datums, esosa_nedelas_diena):
    
    menesu_dienu_skaits = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    
    if type(dzimsanas_gads)!=int or type(dzimsanas_menesis)!=int or type(dzimsanas_datums)!=int or type(esosais_gads)!=int or type(esosais_menesis)!=int or type(esosais_datums)!=int or type(esosa_nedelas_diena)!=int:
        print("Nepareizi ievades dati!")
        return False
        
    if dzimsanas_gads<=0 or dzimsanas_menesis<=0 or dzimsanas_datums<=0 or esosais_gads<=0 or esosais_menesis<=0 or esosais_datums<=0 or esosa_nedelas_diena<=0:
        print("Nepareizi ievades dati!")
        return False

    if dzimsanas_menesis>12 or esosais_menesis>12 or esosa_nedelas_diena>7:
        print("Nepareizi ievades dati!")
        return False
    
    if dzimsanas_datums>menesu_dienu_skaits[dzimsanas_menesis] or esosais_datums>menesu_dienu_skaits[esosais_menesis]:
        print("Nepareizi ievades dati!")
        return False
    
    return True

turpinat = "y"

while turpinat == "y":
    vai_ir_visi_dati = False
    try:
        dzimsanas_gads = int(input("Lūdzu ievadiet savu dzimšanas dienas gadu:"))

        dzimsanas_menesis = int(input("Lūdzu ievadiet savu dzimšanas dienas mēnesi (1-12):"))

        dzimsanas_datums = int(input("Lūdzu ievadiet savu dzimšanas dienas datumu (1-31):"))

        esosais_gads = int(input("Lūdzu ievadiet pašreizējo gadu:"))

        esosais_menesis = int(input("Lūdzu ievadiet pašreizējo mēnesi (1-12):"))

        esosais_datums = int(input("Lūdzu ievadiet šodienas datumu (1-31):"))

        esosa_nedelas_diena = int(input("Lūdzu ievadiet pašreizējo nedēļas dienu (1-7):"))

        vai_ir_visi_dati = True
    except:
        print("Nepareizi ievades dati!")
        vai_ir_visi_dati = False
        

    if vai_ir_visi_dati and ievades_datu_parbaude(esosais_gads, esosais_menesis, esosais_datums, esosa_nedelas_diena, dzimsanas_gads, dzimsanas_menesis, dzimsanas_datums):
        print(dienas_mekletajs(esosais_gads, esosais_menesis, esosais_datums, esosa_nedelas_diena, dzimsanas_gads, dzimsanas_menesis, dzimsanas_datums))

    turpinat = input("Vai vēlies mēģināt vēlreiz? (y/n)")
