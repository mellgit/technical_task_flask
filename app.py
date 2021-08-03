
from flask import Flask, request, abort
from requests import get 
from json import dumps # представить словарь в виде json 
# dump для обратной операции


# get - получить данные со страницы
# post - передать данные на страницу

# объект класса, с параметром основного файла
app = Flask(__name__)

# декоратор для отслеживания определенного url адреса
# декоратор обертка ф-и
@app.route("/")
def index():
    # Анализируемые параметры URL-адреса (часть URL-адреса после вопросительного знака).
    email = request.args.get('email')
    if not email:
        # Flask return 404 - google
        return abort(404)
    

    return abort(400)

if __name__ == '__main__':
    # запуск локального сервера
    app.run(debug=True)