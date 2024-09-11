"""
    Writtn by Juan Pablo Gutiérrez
    10 09 2024
"""

from algorithms.file_manager import getResponse, download, removeFile

from algorithms.code_receiver import getAllCodes

from algorithms.diary_filtering import checkForKeys

from algorithms.mail_sender import send_email

def main(to_email : str):
    codeList = getAllCodes()
    codeList = list(set(codeList))

    email_body = "El programa ha detectado actualizaciones en el DOF con los siguientes códigos de diario:\n\n"

    for code in codeList:
        response = getResponse(code)

        download(code, response)

        result = checkForKeys(code)


        if not result[0]:
            removeFile(code)
            print(f'Code {code} does not have any keys')


        email_body += f"""Código {code} debido a la presencia de las siguientes palabras clave: \n\n"""

        for k, v in result[1].items():
            email_body += f'{k.capitalize()}: {v} ocurrencia(s)\n'

        email_body += f'\nEste archivo está adjunto a este correo, pero se puede acceder a él en la siguiente dirección: https://sidofqa.segob.gob.mx/dof/sidof/documentos/pdf/{code}'

        send_email(subject="Actualización en DOF detectada", body=email_body, to_email=to_email, code=code)

