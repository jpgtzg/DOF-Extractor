"""
    Writtn by Juan Pablo Gutiérrez
    10 09 2024
"""

from downloader import downloadAll

from codeReceiver import getAllCodes

def main():
    codeList = getAllCodes()
    downloadAll(codeList)

if __name__ == '__main__':
    main()