from flask import Flask
import psycopg2

app = Flask(__name__)

def get_name():
    conn = psycopg2.connect(
        host="postgres-db",
        database="mydb",
        user="postgres",
        password="password"
    )

    cur = conn.cursor()

    cur.execute("SELECT name FROM users LIMIT 1;")

    name = cur.fetchone()[0]

    cur.close()
    conn.close()

    return name

@app.route("/")
def home():
    return f"Hello {get_name()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
