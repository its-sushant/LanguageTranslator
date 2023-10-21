from flask import Flask, request, jsonify, render_template
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

    api_url = 'https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e'
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