import requests
from datetime import date

date = date.today().strftime("%d-%m-%Y")

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

print(codeList)

for i in codeList:
    diaryEndpoint = f'https://sidofqa.segob.gob.mx/dof/sidof/documentos/pdf/{
        i}'

    result = requests.get(diaryEndpoint)

    with open('result.pdf', 'wb') as f:
        for chunk in result.iter_content(2000):
            f.write(chunk)
