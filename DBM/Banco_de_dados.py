import dbm
db = dbm.open("captions", "c")

db["zuzu.png"] = "phororo"

for i in range(4):
    db[str(i)] = "num%i" % (i);

for key in db.keys():
    print(key, db[key])
db.close()