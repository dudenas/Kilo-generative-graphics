from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'message': 'Hello from Vercel!', 'status': 'working'})

@app.route('/test')
def test():
    return jsonify({'test': 'success', 'platform': 'vercel'})

if __name__ == '__main__':
    app.run()
