from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
DB_HOST = "mysql-service.default.svc.cluster.local"
DB_ROOT_USER = "root"
DB_ROOT_PASSWORD = "sam123"
DB_NAME = "hello-sql"  # Change this to your preferred database name
NEW_USER = "sumit"
NEW_PASSWORD = "sumit123"

def setup_database():
    try:
        # Connect to MySQL as root
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_ROOT_USER,
            password=DB_ROOT_PASSWORD
        )
        cursor = conn.cursor()

        # Step 1: Create the database if it doesn’t exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")

        # Step 2: Create the user if it doesn’t exist
        cursor.execute(f"CREATE USER IF NOT EXISTS '{NEW_USER}'@'%' IDENTIFIED BY '{NEW_PASSWORD}';")

        # Step 3: Grant privileges to the user on the database
        cursor.execute(f"GRANT ALL PRIVILEGES ON {DB_NAME}.* TO '{NEW_USER}'@'%';")
        cursor.execute("FLUSH PRIVILEGES;")

        conn.commit()
        cursor.close()
        conn.close()
        return f"Database '{DB_NAME}' and user '{NEW_USER}' created successfully."

    except mysql.connector.Error as err:
        return f"Error: {err}"

@app.route("/")
def index():
    result = setup_database()
    return jsonify({"message": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
