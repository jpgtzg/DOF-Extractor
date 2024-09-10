import requests


def getContent(code: int):
    diaryEndpoint = f'https://sidofqa.segob.gob.mx/dof/sidof/documentos/pdf/{
        code}'

    result = requests.get(diaryEndpoint)

    with open('result.pdf', 'wb') as f:
        for chunk in result.iter_content(2000):
            f.write(chunk)
