"""
    Writtn by Juan Pablo Gutiérrez
    10 09 2024
"""

from file_manager import getResponse, download, removeFile

from code_receiver import getAllCodes

from diary_filtering import checkForKeys

def main():
    codeList = getAllCodes()
    codeList = list(set(codeList))

    for code in codeList:
        response = getResponse(code)

        download(code, response)

        if not checkForKeys(code):
            removeFile(code)
            print(f'Code {code} does not have any keys')

    #downloadAll(codeList)

if __name__ == '__main__':
    main()