import shelve as sh

data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 3,
    "f": 2,
    "g": 8,
}
with sh.open("TestDB") as db:
    db.update(data)
    print(db["g"])
