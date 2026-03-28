from flask import Flask, render_template, request
import requests
from googletrans import Translator  # pip install googletrans==4.0.0rc1

app = Flask(__name__)
translator = Translator()


@app.route('/', methods=['GET', 'POST'])
def get_phrase():
    quote = None
    api_key = "rBNlO1h7V5gP3pToRaVwEGJH9p2rwmff9mrgZ14M"
    url = "https://api.api-ninjas.com/v2/quotes?category=philosophy&limit=1"

    if request.method == 'POST':
        headers = {'X-Api-Key': api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            raw_quote = response.json()[0]
            # Переводим quote и author на русский
            translated_quote = translator.translate(raw_quote['quote'], dest='ru').text
            translated_author = translator.translate(raw_quote['author'], dest='ru').text
            quote = {
                'quote': translated_quote,
                'author': translated_author,
                'original_quote': raw_quote['quote'],  # Опционально: оригинал
                'original_author': raw_quote['author']
            }

    return render_template("index.html", quote=quote)


if __name__ == '__main__':
    app.run(debug=True)