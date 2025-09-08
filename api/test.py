import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            'test': 'API connection successful',
            'timestamp': str(datetime.now()),
            'status': 'working',
            'message': 'Hello from Vercel serverless function!'
        }
        
        self.wfile.write(json.dumps(response).encode())
        return