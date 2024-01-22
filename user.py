import sqlite3
from sqlite3 import Error
import csv  # Add this line to import the csv module

def create_connection():
    try:
        con = sqlite3.connect("users.sqlite3")
        return con
    except Error:
        print("Connection Error.")
    except Exception as e:
        print(e)

def create_table(con):
    CREATE_USER_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name CHAR(255) NOT NULL,
        last_name CHAR(255) NOT NULL,
        company_name CHAR(255) NOT NULL,
        address_name CHAR(255) NOT NULL,
        city CHAR(255) NOT NULL,
        county CHAR(255) NOT NULL,
        state CHAR(255) NOT NULL,
        zip INTEGER NOT NULL,
        phone1 CHAR(255) NOT NULL,
        phone2 CHAR(255),
        email CHAR(255) NOT NULL,
        web TEXT    
    );
    """
    cur = con.cursor()
    cur.execute(CREATE_USER_TABLE_QUERY)
    con.commit()  # Commit the changes
    print("Successfully created the table.")

INPUT_STRING = """
Enter the option:
        1. CREATE TABLE
        2. DUMP users from csv INTO users TABLE
        3. ADD new user INTO users TABLE
        4. QUERY all users from TABLE
        5. QUERY user by id from TABLE
        6. QUERY specified no. of records from TABLE
        7. DELETE all users
        8. DELETE user by id
        9. UPDATE user
        10. Press any key to EXIT
"""

def read_csv():
    user_data = []
    with open("sample_users.csv") as f:
        users = csv.reader(f)
        for user in users:
            user_data.append(tuple(user))
    return user_data

def insert_users(con, users):
    user_add_query=""""
    INSERT INTO user
    
    (first_name, last_name, company_name, address, city, county, state, zip, phone1, phone2, email, web)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    
    """
    

def main():
    con = create_connection()
    user_input = input(INPUT_STRING)
    if user_input == "1":
        create_table(con)
    elif user_input == "2":
        read_csv()

if __name__ == "__main__":
    main()
