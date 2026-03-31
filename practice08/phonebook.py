from connect import get_connection

def add_contact(name, phone):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added")

def show_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# test
add_contact("Alihan", "+77051238765")
show_contacts()