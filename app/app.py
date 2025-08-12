from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "testdb")
DB_USER = os.getenv("DB_USER", "user")
DB_PASS = os.getenv("DB_PASS", "pass")

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        now = cur.fetchone()
        cur.close()
        conn.close()
        return f"<h1>Hello from Flask + PostgreSQL!</h1><p>DB Time: {now}</p>"
    except Exception as e:
        return f"<h1>Database connection failed:</h1><pre>{e}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
