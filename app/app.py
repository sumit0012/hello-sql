from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Database connection settings from environment variables
db_config = {
    "host": os.getenv("MYSQL_SERVER", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "password"),
    "database": os.getenv("MYSQL_DB", "test_db")
}

def get_message():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM messages LIMIT 1;")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] if result else "No message found"
    except Exception as e:
        return str(e)

@app.route('/')
def hello():
    return jsonify(message=get_message())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
