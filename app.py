from sys import argv
import sys
import json
from flask import Flask, request, abort
from requests import get 
from json import dumps # представить словарь в виде json 


# необходимые email
email = [
    "eehzntm5@hotmail.com",
    "manuruel@yahoo.com" # not found
    "russellebb912@hotmail.com", # not found
    "jnkitchener@btinternet.com",
    "ras-nie@web.de",
    "ghagen4@gmail.com",
    "mattdhoey@gmail.com"
]

# объект класса, с параметром основного файла
app = Flask(__name__)

# декоратор для отслеживания определенного url адреса
@app.route("/")
def index():

    if sys.argv[1] not in email:
        return abort(404)


    # получить md5 hash
    import hashlib
    hashed_email = hashlib.md5(sys.argv[1].encode('utf-8')).hexdigest()

    # получение json объекта
    response = get(f"https://ru.gravatar.com/{hashed_email}.json")

    if response.status_code == 200:
        need_to_edit = response.json()
        john: dict = need_to_edit['entry'][0]
        new_john = {}
        new_john["id"] = john.get('id', None)
        new_john["email_hash"] = john.get('hash', None)
        new_john["url"] = john.get('profileUrl', None)
        new_john["alias"] = john.get('preferredUsername', None)
        new_john["thumb"] = john.get('thumbnailUrl', None)
        new_john["photos"] = john.get('photos', None)
        new_john["person"] = john.get('name.formatted', None)
        new_john["location"] = john.get('currentLocation', None)
        new_john["emails"] = john.get('emails', None)
        new_john["accounts"] = john.get('accounts', None)
        new_john["urls"] = john.get('urls', None)

        with open("examle.json", "w") as json_file:
            json.dump(new_john, json_file, indent=4)
        
        from pprint import pprint
        pprint(new_john)
        return new_john

    

    return abort(400)

if __name__ == '__main__':
    # запуск локального сервера
    app.run(debug=True, port=5889)