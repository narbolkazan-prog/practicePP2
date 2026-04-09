from connect import connect
import csv

# ---------------- CREATE ----------------
def insert_contact(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Contact added")


def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ CSV imported")


# ---------------- READ ----------------
def get_all_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    print("\n📞 Contacts:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def search_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE name ILIKE %s",
        (f"%{name}%",)
    )

    print(cur.fetchall())

    cur.close()
    conn.close()


def search_by_phone(prefix):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE phone LIKE %s",
        (f"{prefix}%",)
    )

    print(cur.fetchall())

    cur.close()
    conn.close()


# ---------------- UPDATE ----------------
def update_contact(old_name, new_name, new_phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET name=%s, phone=%s WHERE name=%s",
        (new_name, new_phone, old_name)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Contact updated")


# ---------------- DELETE ----------------
def delete_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE name=%s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Contact deleted")


# ---------------- MENU ----------------
def menu():
    while True:
        print("\n==== PHONEBOOK ====")
        print("1. Add contact")
        print("2. Import from CSV")
        print("3. Show all")
        print("4. Search by name")
        print("5. Search by phone")
        print("6. Update contact")
        print("7. Delete contact")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            insert_contact(name, phone)

        elif choice == "2":
            insert_from_csv("contacts.csv")

        elif choice == "3":
            get_all_contacts()

        elif choice == "4":
            name = input("Enter name: ")
            search_by_name(name)

        elif choice == "5":
            prefix = input("Enter phone prefix: ")
            search_by_phone(prefix)

        elif choice == "6":
            old = input("Old name: ")
            new = input("New name: ")
            phone = input("New phone: ")
            update_contact(old, new, phone)

        elif choice == "7":
            name = input("Name to delete: ")
            delete_by_name(name)

        elif choice == "8":
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    menu()