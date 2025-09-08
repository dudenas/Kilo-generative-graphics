from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            'status': 'running',
            'version': '1.2.7',
            'timestamp': str(datetime.now()),
            'message': 'KILO Graphics API is running on Vercel'
        }
        
        self.wfile.write(json.dumps(response).encode())
        return
