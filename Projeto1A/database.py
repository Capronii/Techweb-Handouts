import sqlite3

from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database():
    def __init__(self, name):
        self.name = f'{name}.db'
        self.conn = sqlite3.connect(self.name)
        self.note = self.conn.execute("CREATE TABLE IF NOT EXISTS note(id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);")
        
    def add (self, note: "Note"):
        self.note = self.conn.execute(f"INSERT INTO note (title, content) VALUES ('{note.title}', '{note.content}');")
        self.conn.commit()
    
    def getall(self):
        notes_list = []
        self.cursor = self.conn.execute("SELECT id, title, content FROM note")
        for linha in self.cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id, title, content)
            notes_list.append(note)
        return notes_list
        

    def update(self, entry: "Note"):
        titulo = entry.title
        conteudo = entry.content
        identificador = entry.id
        self.note = self.conn.execute(f"UPDATE note SET title = {titulo}, content = {conteudo} WHERE id = {identificador};")
        self.conn.commit()

    def delete(self, note_id):
        self.note = self.conn.execute(f"DELETE FROM note WHERE id = {note_id};")
        self.conn.commit()