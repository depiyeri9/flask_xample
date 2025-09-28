from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
import mysql.connector

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['BOOTSTRAP_SERVE_LOCAL'] = True

import os
# optional: load environment variables from a .env file if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # python-dotenv not installed or failed to load; environment variables may still be set by the shell
    pass

app.secret_key = os.urandom(24)


def get_db_connection():
    """Create a MySQL connection using environment variables with sensible defaults.

    Environment variables (zsh examples):
      export DB_HOST=localhost
      export DB_USER=root
      export DB_PASSWORD=yourpassword
      export DB_NAME=your_database_name

    If the variables are not set, defaults are used (host=localhost, user=root,
    password=, database=db_task) to make local testing easier.
    """
    host = os.getenv("DB_HOST", "localhost")
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    database = os.getenv("DB_NAME", "db_task")

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )

@app.route("/", methods=["GET", "POST"])
def index():
    search_query = request.args.get("q", "").strip()  # get ?q= from URL
    conn = get_db_connection()
    cursor = conn.cursor()

    if search_query:
        cursor.execute("""
            SELECT id, nama_user, nama_kegiatan, durasi, tanggal_input 
            FROM log_book
            WHERE nama_user LIKE %s OR nama_kegiatan LIKE %s
            ORDER BY tanggal_input DESC
        """, (f"%{search_query}%", f"%{search_query}%"))
    else:
        cursor.execute("""
            SELECT id, nama_user, nama_kegiatan, durasi, tanggal_input 
            FROM log_book
            ORDER BY tanggal_input DESC
        """)

    rows = cursor.fetchall()
    conn.close()
    return render_template("index.html", rows=rows, search_query=search_query)


@app.route("/add", methods=["GET", "POST"])
def add_row():
    if request.method == "POST":
        nama_user = request.form["nama_user"]
        nama_kegiatan = request.form["nama_kegiatan"]
        durasi = request.form["durasi"]
        tanggal_input = request.form["tanggal_input"]

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO log_book (nama_user, nama_kegiatan, durasi, tanggal_input)
            VALUES (%s, %s, %s, %s)
        """, (nama_user, nama_kegiatan, durasi, tanggal_input))
        conn.commit()
        cur.close()
        conn.close()

        flash("Data berhasil ditambahkan!", "success")
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_row(id):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    if request.method == "POST":
        nama_user = request.form["nama_user"]
        nama_kegiatan = request.form["nama_kegiatan"]
        durasi = request.form["durasi"]
        tanggal_input = request.form["tanggal_input"]

        cur.execute("""
            UPDATE log_book
            SET nama_user=%s, nama_kegiatan=%s, durasi=%s, tanggal_input=%s
            WHERE id=%s
        """, (nama_user, nama_kegiatan, durasi, tanggal_input, id))
        conn.commit()
        cur.close()
        conn.close()
        flash("Data berhasil diupdate!", "success")
        return redirect(url_for("index"))

    # ambil data lama buat isi form edit
    cur.execute("SELECT * FROM log_book WHERE id = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return render_template("edit.html", row=row)


@app.route("/delete/<int:id>", methods=["POST"])
def delete_row(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM log_book WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    flash("Data berhasil dihapus!", "danger")
    return redirect(url_for("index"))