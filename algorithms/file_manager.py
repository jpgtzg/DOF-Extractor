"""
    Writtn by Juan Pablo Gutiérrez
    09 09 2024
"""

import requests
import os

def getResponse(code :int) -> requests.models.Response:
    diaryEndpoint = f'https://sidofqa.segob.gob.mx/dof/sidof/documentos/pdf/{code}'
    return requests.get(diaryEndpoint, stream=True)

def download(code : int, result : requests.models.Response, date: str):
    with open(f'{date}-{code}.pdf', 'wb') as f:
        for chunk in result.iter_content(2000):
            f.write(chunk)

def downloadAll(codeList : list):
    for i in codeList:
        download(i)

def removeFile(code : int):
    os.remove(f'{code}.pdf')