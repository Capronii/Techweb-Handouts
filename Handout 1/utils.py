import json
from os import path

def extract_route(requisicao):
    if requisicao.startswith('GET'):
        lista1 = requisicao.split("GET /")
    else:
        lista1 = requisicao.split("POST /")

    lista2 = lista1[1].split(" ")
    return lista2[0]

def read_file(path):
    lista = str(path).split(".")
    if lista[-1]=="txt" or lista[-1]=="html" or lista[-1]=="css" or lista[-1]=="js":
        with open(path, "rb") as file:
            text = file.read()
            return text
    else:
        with open(path, "rb") as file:
            binary = file.read()
        return binary

def load_data(nomeJson):
    filePath = "data/"+nomeJson
    with open(filePath, "rt", encoding="utf-8") as text:
        content = text.read()
        contentPython = json.loads(content)
        return contentPython

def load_template(file_path):
    file = open("templates/"+file_path, encoding="utf-8")
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
    #STR DO CODE
    c = ("{}".format(code))

    if body != "":
        stri = 'HTTP/1.1 200 OK\n\n' + body
    elif code != 200:
        if headers != '':
            stri = "HTTP/1.1" + " " + c + " " +reason + "\n"+ headers + "\n\n"
        else:
            stri = "HTTP/1.1" + " " + c + " " +reason + "\n\n"
    else:
        stri = 'HTTP/1.1 200 OK\n\n'
    return stri.encode()