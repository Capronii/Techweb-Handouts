import json
from database import Database, Note

def extract_route(requisicao):
    if requisicao.startswith('GET'):
        lista1 = requisicao.split("GET /")
    else:
        lista1 = requisicao.split("POST /")

    lista2 = lista1[1].split(" ")
    return lista2[0]


def read_file(path):
    lista = str(path)
    if lista[-1] == "txt" or lista[-1] == "html" or lista[-1] == "css" or lista[-1] == "js":
        with open(path, "rt") as file:
            text = file.read()
            return text
    else:
        with open(path, "rb") as file:
            binary = file.read()
        return binary


def load_data():
    database = Database("Bloco de notas")
    return database.getall()
    # filePath = "data/"+nomeJson
    # with open(filePath, "rt", encoding="utf-8") as text:
    #     content = text.read()
    #     contentPython = json.loads(content)
    #     return contentPython


def load_template(file_path):
    file = open("templates/"+file_path)
    content = file.read()
    file.close()
    return content

def adiciona_nota(nota):
    database = Database("Bloco de notas")
    return database.add(Note(title=nota['titulo'], content=nota['detalhes']))
    # data = load_data('notes.json')
    # data.append(nota)
    # with open ("data/notes.json", "w") as novas_notas:
    #     json.dump(data, novas_notas)


def build_response(body='', code=200, reason='OK', headers=''):
    #'HTTP/1.1 200 OK\n\n'.encode() + response)
    if headers == '':
        return ("HTTP/1.1 " + str(code) + ' ' + reason + "\n\n" + body).encode()
    return ("HTTP/1.1 " + str(code) + ' ' + reason + "\n" + headers + "\n\n" + body).encode()
