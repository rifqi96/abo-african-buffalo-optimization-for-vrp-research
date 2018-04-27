from flask import Flask, request, jsonify
from Main import Main

app = Flask(__name__)

@app.route('/')
def home():
    with app.app_context():
        return jsonify({
            'message':'Welcome to the main app'
        })

if __name__ == '__main__':
    app.run()