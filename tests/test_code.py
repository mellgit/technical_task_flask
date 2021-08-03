from flask import Flask, request, abort
from json import dumps
from requests import get

app = Flask(__name__)


@app.route("/index")
def index():
    email = request.args.get('email')
    if not email:
        # Flask return 404 - google
        return abort(404)

    import hashlib
    hashed_email = hashlib.md5(email.encode('utf-8')).hexdigest()

    response = get(f"https://ru.gravatar.com/{hashed_email}.json")

    if response.status_code == 200:
        need_to_edit = response.json()
        john: dict = need_to_edit['entry'][0]
        new_john = {}
        new_john["id"] = john.get('id', None)
        new_john["hash_email"] = john.get('hash', None)
        from pprint import pprint
        pprint(new_john)
        return new_john

    # Google - flask return status code 400
    return abort(400)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')