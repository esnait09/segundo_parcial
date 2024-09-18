import sqlite3
import json

def load_json_to_database(json_filename, database_filename):
    # Conectar a la base de datos
    connection = sqlite3.connect(database_filename)
    cursor = connection.cursor()

    # Crear la tabla scores si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player TEXT,
            score INTEGER,
            time TEXT,
            level INTEGER
        )
    ''')

    # Leer datos del archivo JSON y insertarlos en la base de datos
    with open(json_filename, 'r') as json_file:
        scores = json.load(json_file)
        for score in scores:
            cursor.execute("INSERT INTO scores (player, score, time, level) VALUES (?, ?, ?, ?)",
                           (score['player'], score['score'], score['time'], score['level']))

    # Guardar los cambios y cerrar la conexión
    connection.commit()
    connection.close()