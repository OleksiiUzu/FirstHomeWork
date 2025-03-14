import sqlite3

def get_db_data(sql_command):
    try:
        connection = sqlite3.connect('Dishes.db')
        print("Database connected to the SQLite.")
        cursor = connection.cursor()
        result = cursor.execute(sql_command)
        print("SQLite is succsesfully executed!")
        data = result.fetchall()
        for i in data:
            print(i)
        return data
    except sqlite3.Error as error:
        print("Error connecting to SQLite.", error)
    finally:
        if connection:
            connection.close()
            print("Connection to SQLite closed.")
