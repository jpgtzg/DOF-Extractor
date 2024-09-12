"""
    Written by Juan Pablo Gutiérrez
    12 09 2024
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

code = ""
with open("315941.pdf", "rb") as file:
    code = file.read()

# Divide the text into smaller chunks
chunks = [code[i:i+1000] for i in range(0, len(code), 1000)]

# Create a list of messages

messages = []
for chunk in chunks:
    messages.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": chunk.decode("utf-8")
                }
            ]
        }
    )


response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages= messages
  
)

print(response.choices[0].message.content)
