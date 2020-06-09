import os
import json

from services import read_replay

from flask import Flask
app = Flask(__name__)

host = os.getenv('HOST') or '0.0.0.0'
port = os.getenv('PORT') or 3000

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/replay')
def replay_info():
    return read_replay('../../LastReplay.w3g')

if __name__ == '__main__':
    app.run(
        host=host,
        port=port
    )

file_path = os.path.basename
print(file_path)