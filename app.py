from flask import Flask, request, jsonify, render_template
from decouple import config
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    sentence = request.form.get('sentence')
    source_lang = request.form.get('sourceLang')
    target_lang = request.form.get('targetLang')

    api_url = config('API_URL')

    data = {
        'sl': source_lang,
        'tl': target_lang,
        'q': sentence,
    }

    response = requests.post(api_url, data=data)
    translation_data = response.json()
    translation = translation_data['sentences'][0]['trans']

    return jsonify({'translation': translation})

if __name__ == '__main__':
    app.run(debug=True)