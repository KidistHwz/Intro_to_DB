import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Your MySQL server host
            user='your_username',  # Your MySQL username
            password='your_password'  # Your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Check if database exists
            cursor.execute("SHOW DATABASES LIKE 'alx_book_store'")
            result = cursor.fetchone()

            if result:
                print("Database 'alx_book_store' already exists.")
            else:
                # Create the database
                cursor.execute("CREATE DATABASE alx_book_store")
                print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()