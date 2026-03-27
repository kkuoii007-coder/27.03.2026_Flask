from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def get_phrase():
   api_key = "ваш_ключ"
   #адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return render_template("index.html", response.json())

if __name__ == '__main__':
   app.run(debug=True)