import mysql.connector
from mysql.connector import Error

DB_NAME = "alx_book_store"

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server (adjust credentials as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password_here"
        )

        # If connection fails, mysql.connector will raise an exception and jump to except block
        cursor = connection.cursor()
        # Create database (no SELECT or SHOW used)
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
        # Commit is not required for CREATE DATABASE but safe to call
        connection.commit()
        print(f"Database '{DB_NAME}' created successfully!")

    except Error as err:
        # Handles connection errors, authentication failures, permission issues, etc.
        print(f"Error while connecting to MySQL or creating database: {err}")

    finally:
        # Close cursor and connection safely (only if they were created)
        try:
            if cursor is not None:
                cursor.close()
        except Exception as close_cursor_err:
            print(f"Error closing cursor: {close_cursor_err}")

        try:
            if connection is not None and connection.is_connected():
                connection.close()
                # Confirm connection was closed
                print("MySQL connection is closed.")
        except Exception as close_conn_err:
            print(f"Error closing connection: {close_conn_err}")

if __name__ == "__main__":
    create_database()
