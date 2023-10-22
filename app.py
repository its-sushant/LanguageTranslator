from flask import Flask, request, jsonify, render_template
from decouple import config
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    request_data = request.get_json()
    sentence = request_data['sentence']
    source_lang = request_data['sourceLang']
    target_lang = request_data['targetLang']

    api_url = config('API_URL')

    data = {
        'sl': source_lang,
        'tl': target_lang,
        'q': sentence,
    }

    response = requests.post(api_url, data=data)
    parsed_response = json.loads(response.text)
    translation = parsed_response['sentences'][0]['trans']

    return jsonify({'translation': translation})

if __name__ == '__main__':
    app.run(debug=True)