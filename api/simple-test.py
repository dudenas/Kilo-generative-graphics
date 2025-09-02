from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'KILO Graphics API is working!',
        'timestamp': str(datetime.now()),
        'status': 'success'
    })

@app.route('/test')
def test():
    return jsonify({
        'test': 'API connection successful',
        'timestamp': str(datetime.now()),
        'endpoints': ['/api/', '/api/test'],
        'status': 'working'
    })

if __name__ == '__main__':
    app.run(debug=True)
