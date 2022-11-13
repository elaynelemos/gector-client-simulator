from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/correct')
def correct_sentence():
    return {
        'msg': 'OK!',
        'datetime': datetime.now()
    }
