import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",               # change this if needed
            password="your_password_here"  # replace with your MySQL root password
        )

        # If the connection was successful
        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle connection or creation errors
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the cursor and connection safely
        try:
            if cursor:
                cursor.close()
        except NameError:
            pass  # cursor not defined if connection failed

        try:
            if connection and connection.is_connected():
                connection.close()
                print("MySQL connection is closed.")
        except NameError:
            pass  # connection not defined if connection failed

if __name__ == "__main__":
    create_database()
