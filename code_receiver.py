"""
    Writtn by Juan Pablo Gutiérrez
    09 09 2024
"""

import requests
from datetime import datetime

def getAllCodes() -> list:
    date = datetime.today().strftime("%d-%m-%Y")
    
    dateEndpoint = f'https://sidofqa.segob.gob.mx/dof/sidof/diarios/porFecha/{
        date}'
    x = requests.get(dateEndpoint).json()

    matutina = x["Matutina"]
    vespertina = x["Vespertina"]
    extraordinaria = x["Extraordinaria"]

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