""" 
    Written by Juan Pablo Gutiérrez
    10 09 2024
"""

import requests
from pypdf import PdfReader
from collections import defaultdict

key = ["Fugas", "Registradores", "Telemetría", "Dataloggers", "Eficiencia", "Correlador", "Geófono", "Multicorrelador", "Logger", "Pérdidas", "Recuperación"]


def checkForKeys(code: int) -> bool:
    lower_keys = [k.lower() for k in key]  # Convert keys to lowercase
    foundKeys = defaultdict(int)  # Initialize a defaultdict to count occurrences

    reader = PdfReader(f'{code}.pdf')

    for page in reader.pages:
        content = page.extract_text().lower()

        for i in lower_keys:
            if i in content:
                foundKeys[i] += 1  # Increment the count for the key

    print(f'Code {code} has the following keys:')
    for k, v in foundKeys.items():
        print(f'{k}: {v}')

    return len(foundKeys) > 0
