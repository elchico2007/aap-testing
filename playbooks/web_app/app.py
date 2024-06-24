from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/dadjoke')
def get_dad_joke():
    headers = {'Accept': 'text/plain'}
    response = requests.get('https://icanhazdadjoke.com/', headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return jsonify({'error': 'Failed to fetch a joke'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

