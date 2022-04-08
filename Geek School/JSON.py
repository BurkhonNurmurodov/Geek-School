import json as js

def get_from_json(filename):
    with open(filename) as file:
        res = js.load(file)
    return res

def add_to_json(filename, data):
    with open(filename, "w") as file:
        js.dump(data, file)

def check(type:str="user", id=int):
    users = get_from_json(f"{type}s.json")
    b = False
    for i in users:
        if i['id'] == id:
            b = True
            break
    return b

def find(type:str="user", id=int):
    users = get_from_json(f"{type}s.json")
    for i in range(len(users)):
        if users[i]['id'] == id:
            break
    return i