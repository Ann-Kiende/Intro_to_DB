import mysql.connector

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",               # Change if needed
            password="your_password_here"  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it does not exist
            # (No SELECT or SHOW statements used)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Handle MySQL-related errors
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Safely close cursor and connection
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
