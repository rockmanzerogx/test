
import json
import re
import requests

mensaje = "Hola mundo"

url = 'http://localhost:11434/api/generate'
headers = {'Content-Type': 'application/json'}

data = {
    "model": "deepseek-r1:1.5b",
    "prompt": mensaje,	
    "stream": False,
    "options": {"temperature":0}
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print('Respuesta:', response.text)
respuesta_texto=json.loads(response.text)['response']
print(respuesta_texto)
filtered_text = re.sub(r'<think>,*?</think>', '', respuesta_texto, flags=re.DOTALL)
print(filtered_text.strip())