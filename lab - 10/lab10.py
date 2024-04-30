import psycopg2
import csv

def connect():
    return psycopg2.connect(
        dbname="phonebook",
        user="postgres",
        password="fake1205",
        host="127.0.0.1",
    )

def create_contacts_table():
    try:
        conn = connect()
        cursor = conn.cursor()

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS Contacts (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                phone_number VARCHAR(15)
            )
        '''
        cursor.execute(create_table_query)
        conn.commit()
        print("Contacts table created successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def upload_from_csv(filename):
    try:
        conn = connect()
        cursor = conn.cursor()
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                cursor.execute("INSERT INTO Contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
            conn.commit()
        print("Data uploaded successfully from CSV.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def insert_from_console():
    try:
        conn = connect()
        cursor = conn.cursor()
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        cursor.execute("INSERT INTO Contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first_name, last_name, phone_number))
        conn.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def update_contact(contact_id, new_first_name=None, new_last_name=None, new_phone_number=None):
    try:
        conn = connect()
        cursor = conn.cursor()

        update_query = "UPDATE Contacts SET"
        if new_first_name:
            update_query += " first_name = %s,"
        if new_last_name:
            update_query += " last_name = %s,"
        if new_phone_number:
            update_query += " phone_number = %s,"

        update_query = update_query[:-1]  # Remove trailing comma
        update_query += " WHERE id = %s"

        cursor.execute(update_query, (new_first_name, new_last_name, new_phone_number, contact_id))
        conn.commit()
        print("Contact updated successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def query_contacts(filter_type, filter_value):
    try:
        conn = connect()
        cursor = conn.cursor()

        if filter_type == "first_name":
            cursor.execute("SELECT * FROM Contacts WHERE first_name = %s", (filter_value,))
        elif filter_type == "last_name":
            cursor.execute("SELECT * FROM Contacts WHERE last_name = %s", (filter_value,))
        elif filter_type == "phone_number":
            cursor.execute("SELECT * FROM Contacts WHERE phone_number = %s", (filter_value,))
        else:
            print("Invalid filter type.")
            return

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

def delete_contact(filter_type, filter_value):
    try:
        conn = connect()
        cursor = conn.cursor()

        if filter_type == "first_name":
            cursor.execute("DELETE FROM Contacts WHERE first_name = %s", (filter_value,))
        elif filter_type == "last_name":
            cursor.execute("DELETE FROM Contacts WHERE last_name = %s", (filter_value,))
        elif filter_type == "phone_number":
            cursor.execute("DELETE FROM Contacts WHERE phone_number = %s", (filter_value,))
        else:
            print("Invalid filter type.")
            return

        conn.commit()
        print("Contact(s) deleted successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# Create Contacts table
create_contacts_table()

insert_from_console()