import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database():
    def __init__(self,banco):
        self.banco=banco
        self.conn=sqlite3.connect(self.banco+".db")
        self.create=("CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,  title TEXT ,content TEXT NOT NULL);")
        self.conn.execute(self.create)

    def add(self,note):
        self.conn.execute(
            ("INSERT INTO note (title, content)  VALUES ('{}', '{}');").format(note.title,note.content)
        )
        self.conn.commit()

    def get_all(self):
        c=self.conn.execute("SELECT id, title, content FROM note;")
        list = []
        for linha in c:
            id=linha[0]
            title=linha[1]
            content=linha[2]
            list.append(Note(id=id,title=title,content=content))
        return list

    def update(self,entry):
        self.entry=entry
        do_update=("UPDATE note SET title='{}', content = '{}' WHERE id = {};").format(entry.title,entry.content,entry.id)
        self.conn.execute(do_update)
        self.conn.commit()

    def delete(self,note_id):
        do_delete=(f"DELETE FROM note WHERE id = {note_id};")
        self.conn.execute(do_delete)
        self.conn.commit()


