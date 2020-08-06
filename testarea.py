from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()
q1 = db.remove(User.name == 'a')
if q1:
    print("q1 is filled")
else:
    print("q1 is empty")
