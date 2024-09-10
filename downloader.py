"""
    Writtn by Juan Pablo Gutiérrez
    09 09 2024
"""

import requests

def download(code : int):
    diaryEndpoint = f'https://sidofqa.segob.gob.mx/dof/sidof/documentos/pdf/{code}'
    result = requests.get(diaryEndpoint)
    with open(f'{code}.pdf', 'wb') as f:
        for chunk in result.iter_content(2000):
            f.write(chunk)


def downloadAll(codeList : list):
    for i in codeList:
        download(i)