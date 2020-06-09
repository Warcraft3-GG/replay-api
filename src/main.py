import os
import json
from flask import Flask
app = Flask(__name__)

host = os.getenv('HOST') or '0.0.0.0'
port = os.getenv('PORT') or 3000

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(
        host=host,
        port=port
    )
