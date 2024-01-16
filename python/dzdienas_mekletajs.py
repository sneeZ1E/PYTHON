def dienas_mekletajs (esosais_gads, esosais_menesis, esosais_datums, esosa_diena, dzimsanas_gads, dzimsanas_menesis, dzimsanas_datums):
    menesu_dienu_skaits = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
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


    #Tiek skaitits cik pilni menesi pagajusi kops dzd
    #Tiek skaitits cik dienas pari pilniem menesiem ir pagajusas

    return "harosh"


def vai_datums_jau_pagajis(esosais_menesis, esosais_datums, dzimsanas_menesis, dzimsanas_datums):
    if esosais_menesis>dzimsanas_menesis:
        return True
    if esosais_menesis<dzimsanas_menesis:
        return False
    if esosais_datums<dzimsanas_datums:
        return False
    return True