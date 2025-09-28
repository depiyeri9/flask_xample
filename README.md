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
# Flask — README (beginner friendly)

This is a very small Flask app that stores a simple "log book" in a MySQL database. This README explains, in plain language, how to get the app working on macOS (zsh). The configuration is dynamic — you do not need to edit Python files to set your database credentials.

## Quick overview (what this project contains)

- `init.py` — the Flask application entry point (reads DB config from environment variables).
- `requirements.txt` — Python packages required by the app.
- `log_book_202509281932.sql` — SQL dump to create the project's database and `log_book` table.
- `templates/` — HTML templates used by the web pages (`index.html`, `add.html`, `edit.html`).

## What you need (prerequisites)

- Python 3.8+ installed (3.11 recommended). Check with `python3 --version`.
- MySQL server installed and running (or MariaDB). You need a user with privileges to create a database and import the SQL file.
- A terminal using zsh (this README uses zsh commands).

## Step-by-step setup (for dummies)

1) Open Terminal (zsh)

2) Change to the project folder in your terminal:

```zsh
# example: update the path to where you have the project
cd /path/to/this/project
```

3) Create and activate a Python virtual environment (recommended):

```zsh
python3 -m venv .venv
source .venv/bin/activate
```

4) Install the required Python packages:

```zsh
pip install --upgrade pip
pip install -r requirements.txt
```

5) Create the MySQL database and import the table structure/data using the provided SQL file

- Start your MySQL server (if it isn't running).
- Pick a name for the database and import the SQL dump. Replace DB_NAME with your chosen name:

```zsh
DB_NAME=azam_prokom_local
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"
mysql -u root -p $DB_NAME < log_book_202509281932.sql
```

You will be prompted for the MySQL password when using `-p`.

If you use a different MySQL user than `root`, pass `-u youruser` and provide that user's password when prompted, or use environment variables as described below.

6) Configure database credentials (recommended: environment variables)

The app reads DB credentials from environment variables. This is safer and more portable than editing code.

Environment variables used by the app (defaults shown):

- `DB_HOST` (default: `localhost`)
- `DB_USER` (default: `root`)
- `DB_PASSWORD` (default: `rootr00t`)
- `DB_NAME` (default: `azam_prokom_04_09_25`)

Set them in zsh like this:

```zsh
export DB_HOST=localhost
export DB_USER=root
export DB_PASSWORD=your_mysql_password
export DB_NAME=azam_prokom_local
```

Alternatively, copy the included `.env.example` to `.env` and edit it:

```zsh
cp .env.example .env
# edit .env with your values
```

Note: The app will attempt to load `.env` if `python-dotenv` is installed. Installing `python-dotenv` is optional — you can also set variables in your shell.

To install python-dotenv (optional):

```zsh
pip install python-dotenv
```

7) Run the app

With your virtualenv activated and the DB/import done, run:

```zsh
# tell Flask which file contains the app
export FLASK_APP=init.py
# optional: enable development mode (shows debug output)
export FLASK_ENV=development

flask run
```

Open a browser and go to http://127.0.0.1:5000/ to see the app.

If the `flask` command is not available inside the virtualenv, run:

```zsh
python -m flask run
```

## What the app does (simple)

- The main page lists rows from the `log_book` table.
- Use the Add page to insert a new record (name, activity, duration, date).
- Each row can be edited or deleted from the UI.
- There's a search box that filters by user name or activity.

## Troubleshooting (common beginner issues)

- "Can't connect to MySQL": Check MySQL is running and that `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME` are set correctly.
- `ModuleNotFoundError` for a package: activate your virtualenv and run `pip install -r requirements.txt`.
- Permission errors when importing SQL: ensure the MySQL user has CREATE and INSERT privileges or run import as a privileged user.
- If `flask` command not found: make sure your virtualenv is activated, or run `python -m flask run` instead.

## Notes & security

- The app uses a random secret key for local testing. For production, set a fixed secret via environment variables and keep it private.
- Do not commit real database passwords to source control. Use environment variables or a secrets manager.

## Next steps (optional improvements)

- Add a `.env` and update the project to read other configuration (e.g., SECRET_KEY) from environment variables.
- Add authentication to protect the UI.

If you'd like, I can update `init.py` to read the Flask secret key from an environment variable and add a `.env.example` file (I will add one by default here).

---

Follow the steps above and you should be able to run the app locally. If something fails, copy the error and paste it here and I'll help you fix it.
