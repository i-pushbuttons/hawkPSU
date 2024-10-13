from flask import Flask, jsonify
from flask_cors import CORS
from ai import generate_integral_problem

app = Flask(__name__)
CORS(app)


@app.route('/generate-problem', methods=['GET'])
def generate_problem():
    problem = generate_integral_problem()
    return jsonify({'problem': problem})

if __name__ == '__main__':
    app.run(port=5000)