import json
from flask import Flask, request

app = Flask(__name__)

d = {
    'fen': 'rnbqkbnrpppppppp11111111111111111111111111111111PPPPPPPPRNBQKBNR'
}


@app.route('/write_json', methods=['POST'])
def write_json():
    data = request.get_json()

    file_path = 'chess.json'

    with open(file_path, 'w') as f:
        json.dump(data, f)

    return 'Данные успешно записаны в файл JSON.'


if __name__ == '__main__':
    app.run(debug=True)
