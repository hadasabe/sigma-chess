from flask import Flask, render_template, url_for, request
import jinja2

app = Flask(__name__)


@app.route('/')
def home():
    return '<a href="/game">game</a>'


@app.route('/game')
def game():

    return render_template('game.html')