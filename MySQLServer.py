import mysql.connector

def create_database():
    connection = None
    cursor = None
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",               # change if needed
            password="your_password_here"  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database (no SELECT or SHOW statements used)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Explicitly handle mysql.connector.Error exceptions
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure cursor and connection are closed properly
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
