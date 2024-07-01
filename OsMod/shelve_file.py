import shelve as sh

with sh.open("testDB.db") as db:
    db["a"] = 1
    db["b"] = 2
    db["c"] = 3
    db["d"] = 4
    db["e"] = 5
with sh.open("testDB") as db:
    print(dict(db))
    print(db["a"])
