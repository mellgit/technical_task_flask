import sys
import json
from requests import get 
from json import dumps # представить словарь в виде json


# получить md5 hash
import hashlib
hashed_email = hashlib.md5(sys.argv[1].encode('utf-8')).hexdigest()

# получение json объекта
response = get(f"https://ru.gravatar.com/{hashed_email}.json")

# преобразование необходимого json
if response.status_code == 200:
    need_to_edit = response.json()
    result: dict = need_to_edit['entry'][0]
    new_result = {}
    new_result["id"] = result.get('id', None)
    new_result["email_hash"] = result.get('hash', None)
    new_result["url"] = result.get('profileUrl', None)
    new_result["alias"] = result.get('preferredUsername', None)
    new_result["thumb"] = result.get('thumbnailUrl', None)
    new_result["photos"] = result.get('photos', None)
    new_result["person"] = result.get('name.formatted', None)
    new_result["location"] = result.get('currentLocation', None)
    new_result["emails"] = result.get('emails', None)
    new_result["accounts"] = result.get('accounts', None)
    new_result["urls"] = result.get('urls', None)

    # запись в json file
    with open("result_script.json", "w") as json_file:
        json.dump(new_result, json_file, indent=4)

    # красивый вывод
    from pprint import pprint
    pprint(new_result)

else:
    print("Gravatar error")
    print("Something went wrong, sry")