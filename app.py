from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_equipos():
    conn = sqlite3.connect('database/inventario.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipos")
    equipos = cursor.fetchall()
    conn.close()
    return equipos

@app.route('/')
def index():
    equipos = get_equipos()
    return render_template('index.html', equipos=equipos)

if __name__ == '__main__':
    app.run(debug=True)
