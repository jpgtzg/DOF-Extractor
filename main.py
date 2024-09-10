"""
    Writtn by Juan Pablo Gutiérrez
    10 09 2024
"""

from downloader import downloadAll, getResponse, download

from code_receiver import getAllCodes

from diary_filtering import checkForKeys
def main():
    codeList = getAllCodes()

    for code in codeList:
        response = getResponse(code)

        download(code, response)
    
        checkForKeys(code)

    #downloadAll(codeList)

if __name__ == '__main__':
    main()