from pathlib import Path
import json

def extract_route(request):
    if request.startswith('GET'):
        lista1 = request.split("GET /")
    else:
        lista1 = request.split("POST /")

    lista2 = lista1[1].split(" ")
    return lista2[0]

def read_file(filepath):
    if filepath.suffix in ['.txt', '.html', '.css', '.js']:
        mode = 'r'
    else:
        mode = 'rb'

    with open(filepath, mode=mode) as f:
        return f.read()

def load_data(nomeJson):
    filePath = "data/"+nomeJson
    with open(filePath, "rt", encoding="utf-8") as text:
        content = text.read()
        contentPython = json.loads(content)
        return contentPython
def load_template(file_path):
    file = open("templates/"+file_path)
    content = file.read()
    file.close()
    return content

def recebe_post(params):
    filename = 'data/notes.json'
    entry ={
    "titulo": params['titulo'],
    "detalhes": params['detalhes']
  }
    with open(filename, "rt", encoding="utf-8") as file:
        data = json.load(file)
    data.append(entry)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        headers=f"\n{headers}"
    response = f"HTTP/1.1 {code} {reason}{headers}\n\n{body}".encode()
    return response

