from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
import mysql.connector

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['BOOTSTRAP_SERVE_LOCAL'] = True

import os
app.secret_key = os.urandom(24)


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='rootr00t',
        database='azam_prokom_04_09_25'
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM log_book")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("read.html", rows=rows)


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
