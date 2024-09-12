"""
    Writtn by Juan Pablo Gutiérrez
    09 09 2024
"""

import requests

def getAllCodes(date: str) -> list:
    
    dateEndpoint = f'https://sidofqa.segob.gob.mx/dof/sidof/diarios/porFecha/{
        date}'
    x = requests.get(dateEndpoint).json()

    matutina = []
    vespertina = []
    extraordinaria = []
    try:
        matutina = x["Matutina"]
        vespertina = x["Vespertina"]
        extraordinaria = x["Extraordinaria"]
    except:
        print("No data found")
        return []

    codeList = list()

    if matutina:
        for i in matutina:
            codeList.append(i["codDiario"])

    if vespertina:
        for i in vespertina:
            codeList.append(i["codDiario"])


    if extraordinaria:
        for i in extraordinaria:
            codeList.append(i["codDiario"])

    return codeList