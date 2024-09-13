""" 
    Written by Juan Pablo Gutiérrez
    10 09 2024
"""

from pypdf import PdfReader
from collections import defaultdict
import re

keys = ["Fugas", "Registradores", "Telemetría", "Dataloggers", "Eficiencia", "Correlador", "Geófono", "Multicorrelador", "Logger", "Pérdidas", "Recuperación"]

def checkForKeys(code: int) -> tuple:
    lower_keys = [k.lower() for k in keys]  # Convert all keys to lowercase
    foundKeys = defaultdict(int)
    context_sentences = []

    reader = PdfReader(f'{code}.pdf')

    for page in reader.pages:
        content = page.extract_text().lower()
        sentences = re.split(r'(?<=[.!?]) +', content)  # Split content into sentences

        for i in lower_keys:
            for sentence in sentences:
                if i in sentence:
                    foundKeys[i] += 1
                    # Extract 40 words before and after the key
                    words = sentence.split()
                    key_index = sentence.find(i)
                    start = max(0, key_index - 80)
                    end = min(len(sentence), key_index + len(i) + 80)
                    context = sentence[start:end]
                    context_sentences.append((i, context))

    return (len(foundKeys) > 0, dict(foundKeys), context_sentences)