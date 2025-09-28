# Flask — README

This is a very small Flask app that stores a simple "log book" in a MySQL database.
This README explains, in plain language, how to get the app working on your macOS machine using zsh.

If you are new to programming or new to this project, follow the steps exactly and you'll be up and running.

## Quick overview (what this project contains)

- `init.py` — the Flask application entry point.
- `requirements.txt` — Python packages required by the app.
- `log_book_202509281932.sql` — SQL dump to create the project's database and `log_book` table.
- `templates/` — HTML templates used by the web pages (`index.html`, `add.html`, `edit.html`).

## What you need (prerequisites)

- Python 3.8+ installed (3.11 recommended). Check with `python3 --version`.
- MySQL server installed and running (or MariaDB). You need a user with privileges to create a database and import the SQL file.
- A terminal using zsh (this README uses zsh commands).

If you're not sure how to install Python or MySQL, search for "install Python on macOS" and "install MySQL on macOS" — there are many tutorials.

## Step-by-step setup (for dummies)

1. Open Terminal (zsh).

2. Clone or open this project folder (you already have it opened):

```zsh
# change to the project folder
cd /path/to/project
```

3. Create and activate a Python virtual environment (recommended):

```zsh
python3 -m venv .venv
source .venv/bin/activate
```

4. Install the required Python packages:

```zsh
pip install --upgrade pip
pip install -r requirements.txt
```

5. Create the MySQL database and import the table structure/data using the provided SQL file.

- Start your MySQL server (if it isn't running).
- If you have `root` MySQL user with password `rootr00t` (this project uses these credentials by default in `init.py`), you can run:

```zsh
# Create the database (if not present) and import the SQL file
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS azam_prokom_04_09_25;"
mysql -u root -p azam_prokom_04_09_25 < log_book_202509281932.sql
```

You will be prompted for the MySQL password when using `-p`.

If your MySQL root password or username is different, change the `-u` and either pass the correct username/password or edit `init.py` to match your DB user. See next section.

6. Edit database credentials (if needed)

Open `init.py` and find the function `get_db_connection()` — change `host`, `user`, `password`, and `database` to match your local MySQL setup.

Example (inside `init.py`):

```py
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='rootr00t',
        database='azam_prokom_04_09_25'
    )
```

Tip: If you prefer not to hard-code credentials in the file, you can set environment variables and modify the file to read them. For beginners, editing `init.py` directly is the simplest.

7. Run the app

With your virtualenv activated and after the DB is imported, run:

```zsh
# tell Flask which file contains the app
export FLASK_APP=init.py
# optional: enable development mode (shows debug output)
export FLASK_ENV=development

flask run
```

Open a browser and go to http://127.0.0.1:5000/ to see the app.

If `flask run` fails, you can also run with Python directly (Flask picks up the `app` in `init.py` when using `flask run` — the direct method below works as a fallback):

```zsh
python -m flask run
```

## What the app does (simple)

- The main page lists rows from the `log_book` table.
- Use the Add page to insert a new record (name, activity, duration, date).
- Each row can be edited or deleted from the UI.
- There's a search box that filters by user name or activity.

## Files you might edit next (for learning)

- `init.py` — the main code; add logging or modify routes.
- `templates/*.html` — change the UI text or layout.

## Troubleshooting (common beginner issues)

- "Can't connect to MySQL": Check MySQL is running and credentials are correct in `init.py`.
- `ModuleNotFoundError` for a package: activate your virtualenv and run `pip install -r requirements.txt`.
- Permission errors when importing SQL: ensure the MySQL user has CREATE and INSERT privileges or run import as a privileged user.
- If `flask` command not found: make sure your virtualenv is activated, or run `python -m flask run` instead.

## Notes & security

- This project hard-codes a random secret key using `os.urandom(24)` (fine for local testing). For production, set a proper secret via env vars.
- Do not ship database passwords inside code for real projects; use environment variables or a secrets manager.

## Where to go from here (next steps)

- Try editing `templates/index.html` to change the page title.
- Add server-side validation or authentication if you want to protect the UI.
- Move DB credentials to environment variables and read them from `init.py`.

If you want, I can:

- add a small `.env`-based config and show how to use it, or
- modify `init.py` to read DB credentials from environment variables and provide an example `.env` file.

---

That's it — follow the steps above and you should be able to run the app locally. If something fails, copy the error and paste it here and I'll help you fix it.
