import csv
from connect import connect

conn = connect()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(20)
)
""")

with open("practice07/contacts.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
            (row["name"], row["phone"])
        )

conn.commit()

cur.execute("SELECT * FROM phonebook")
rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()
conn.close()