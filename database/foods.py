import sqlite3
from flask import jsonify


class alimentos():
    def __init__(self, gramas, nome, carb, prot, fat):
        self.gramas = gramas
        self.nome = nome
        self.carb = carb
        self.prot = prot
        self.fat = fat

        conn = sqlite3.connect('dbAlimentos.db')
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS alimentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gramas INTEGER NOT NULL,
                calorias REAL NOT NULL,
                nome TEXT NOT NULL,
                carboidratos REAL NOT NULL,
                proteinas REAL NOT NULL, gorduras REAL NOT NULL )""")
        conn.commit()
        conn.close()

    def inserirAlimento(self, calorias):
        conn = sqlite3.connect('dbAlimentos.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alimentos (gramas, calorias, nome, carboidratos, proteinas, gorduras) VALUES (?, ?, ?, ?, ?, ?)",
                       (self.gramas, calorias, self.nome, self.carb, self.prot, self.fat))
        conn.commit()
        conn.close()

    # def listarAlimento(self):
    #     conn = sqlite3.connect('dbAlimentos.db')
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT nome, calorias, gramas FROM alimentos")
    #     foods = cursor.fetchall()
    #     conn.close()
        
        



    
