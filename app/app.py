from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
DB_HOST = "mysql.hwsql.svc.cluster.local"
DB_ROOT_USER = "root"
DB_ROOT_PASSWORD = "sam123"
DB_NAME = "hello_sql"
NEW_USER = "sumit"
NEW_PASSWORD = "sumit123"

def setup_database():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_ROOT_USER,
            password=DB_ROOT_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        # ✅ Ensure the messages table exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # ✅ Check if message exists
        cursor.execute("SELECT COUNT(*) FROM messages;")
        count = cursor.fetchone()[0]

        if count == 0:
            cursor.execute("INSERT INTO messages (content) VALUES ('Hello-world from CodeFrontier');")
            conn.commit()

        # ✅ Fetch the message from the database
        cursor.execute("SELECT content FROM messages ORDER BY id DESC LIMIT 1;")
        message = cursor.fetchone()[0]

        cursor.close()
        conn.close()
        return message

    except mysql.connector.Error as err:
        return f"Database connection failed: {err}"

@app.route("/")
def index():
    result = setup_database()
    return jsonify({"message": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)