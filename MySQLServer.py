import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password"
    )

    cursor = connection.cursor()

    
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
