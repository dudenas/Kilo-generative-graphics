from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

def handler(request):
    return jsonify({
        'test': 'API connection successful',
        'timestamp': str(datetime.now()),
        'status': 'working',
        'message': 'Hello from Vercel serverless function!'
    })