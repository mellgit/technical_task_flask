from flask import Flask

# объект класса, с параметром основного файла
app = Flask(__name__)

# декоратор для отслеживания определенного url адреса
# декоратор обертка ф-и
@app.route("/")
def index():
    return 'hello world'

if __name__ == '__main__':
    # запуск локального сервера
    app.run(debug=True)