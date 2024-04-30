from flask import Flask, render_template, url_for, request, jsonify, send_from_directory, redirect

import sqlite3
import jinja2
import berserk
import json
import bcrypt

app = Flask(__name__)

connection = sqlite3.connect('db/db.db', check_same_thread=False)
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
password TEXT NOT NULL
)
''')

connection.commit()


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/profile')
# def profile():
#     return render_template('profile.html')


@app.route('/profile', methods=['POST'])
def profile():
    username = request.form['username']
    password = request.form['password']

    hash_password = bcrypt.hashpw('userPlainTextPassword'.encode(), bcrypt.gensalt())
    cursor.execute('INSERT INTO Users (username, password) VALUES (?, ?)', (str(username), hash_password))
    connection.commit()

    users = list(cursor.execute('SELECT username, password FROM Users'))
    print(list(users))

    if username and password:
        for i in range(len(users)):
            valid = bcrypt.checkpw(password.encode(), users[i][1])
            if username == users[i][0] and valid:
                print(valid)
                r(username)
                return redirect(url_for('r'))
            else:
                return redirect(url_for('auth'))
    else:
        return redirect(url_for('auth', _external=True))


@app.route('/r/<string:username>')
def r(username):
    return username

@app.route("/str-url/<string:str_params>")
def String_Func(str_params):
    return "The string parameter is: " + str_params

@app.route('/auth')
def login():
    return render_template('login.html')


@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/get_fen', methods=['POST'])
def get_fen():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print("Received JSON data:", data)

            fen = data['fen']

            d = {'fen': fen}
            
            with open('static/chess.json', 'w') as file:
                json.dump(d, file)
                file.close()

            return jsonify(success=True)
        except Exception as e:
            print("Error:", e)
            return jsonify(success=False, error=str(e))


if __name__ == '__main__':
    app.run(debug=True)