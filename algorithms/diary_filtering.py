""" 
    Written by Juan Pablo Gutiérrez
    10 09 2024
"""

from pypdf import PdfReader
from collections import defaultdict

key = ["Fugas", "Registradores", "Telemetría", "Dataloggers", "Eficiencia", "Correlador", "Geófono", "Multicorrelador", "Logger", "Pérdidas", "Recuperación"]

def checkForKeys(code: int) -> tuple:
    lower_keys = [k.lower() for k in key]  # Convert all keys to lowercase
    foundKeys = defaultdict(int)

    reader = PdfReader(f'{code}.pdf')

    for page in reader.pages:
        content = page.extract_text().lower()

        for i in lower_keys:
            if i in content:
                foundKeys[i] += 1

    return (len(foundKeys) > 0, dict(foundKeys))
