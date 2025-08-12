import os
import psycopg2

def test_db_connect():
    # Connect directly to the CI Postgres service using env set in the workflow
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "testdb"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASS", "pass"),
    )
    with conn.cursor() as cur:
        cur.execute("SELECT 1;")
        assert cur.fetchone()[0] == 1
    conn.close()

def test_http_root():
    # Import the Flask app and do a simple HTTP request to "/"
    from app.app import app
    with app.test_client() as c:
        r = c.get("/")
        assert r.status_code == 200
