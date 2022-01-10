from flask import Flask
from flask import jsonify
import random

app = Flask(__name__)


@app.route('/get_random/', methods=['GET', 'POST'])
def welcome():
    return jsonify({
        'randon_number': random.random()
    } )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1112)
