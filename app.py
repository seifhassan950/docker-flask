from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_name():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    cur = conn.cursor()

    cur.execute("SELECT name FROM users LIMIT 1;")

    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        return result[0]
    else:
        return "World"

@app.route("/")
def home():
    return f"Hello {get_name()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
