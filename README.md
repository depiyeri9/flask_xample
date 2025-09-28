# Flask — README

This is a very small Flask app that stores a simple "log book" in a MySQL database.
This README explains, in plain language, how to get the app working on your macOS machine using zsh.

If you are new to programming or new to this project, follow the steps exactly and you'll be up and running.

## Quick overview (what this project contains)

- `init.py` — the Flask application entry point.
# Simple README — for absolute beginners

This project is a tiny Flask app that stores a "log book" in MySQL. If you are new to programming, follow these exact steps. Copy-paste the commands into your terminal.

If something does not work, copy the error message and share it and I will help.

## What is here

- `init.py` — the app code (reads database settings from environment variables).
- `requirements.txt` — packages to install.
- `log_book_202509281932.sql` — database structure and sample data.
- `templates/` — HTML pages used by the app.

## Step 0 — open terminal and go to the project

Open Terminal (zsh). Then change to the project folder (replace the path):

```zsh
cd /path/to/this/project
```

Examples below assume you run commands from the project folder.

## Step 1 — create a virtual environment and install packages

```zsh
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

If any command fails, copy the error and paste it here.

## Step 2 — create the database and import the data (copy-paste)

Pick a name for your database. We will use `my_logbook` as an example.

```zsh
DB_NAME=my_logbook
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"
mysql -u root -p $DB_NAME < log_book_202509281932.sql
```

- You will be asked for your MySQL password after `-p`.
- If you do not use `root`, replace `-u root` with `-u your_mysql_user`.

If you see "Access denied", use a MySQL user with the right privileges or ask someone who manages the database for help.

## Step 3 — tell the app how to connect to the database (two easy ways)

Option A — quick (temporary) using shell variables

Run these commands in the same terminal window where you will start the app. Replace values with your MySQL info:

```zsh
export DB_HOST=localhost
export DB_USER=root
export DB_PASSWORD=your_mysql_password
export DB_NAME=my_logbook
```

Option B — copy `.env.example` to `.env` and edit (recommended for beginners who prefer a file)

```zsh
cp .env.example .env
# open .env in a text editor and change DB_PASSWORD and DB_NAME
```

Note: the app will try to load `.env` automatically if you install `python-dotenv` (optional). To install it:

```zsh
pip install python-dotenv
```

Either option works. If you use Option A, the variables last only for that terminal session. If you want them every time you open a terminal, add the export lines to `~/.zshrc`.

## Step 4 — start the app

In the same terminal (with the virtualenv active and environment variables set), run:

```zsh
export FLASK_APP=init.py
export FLASK_ENV=development    # optional: shows helpful debug info
flask run
```

Open your web browser and go to: http://127.0.0.1:5000/

If `flask` is not found, run:

```zsh
python -m flask run
```

## Very short troubleshooting

- "Can't connect to MySQL": verify `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` are correct and MySQL server is running.
- `ModuleNotFoundError`: make sure virtualenv is active and you ran `pip install -r requirements.txt`.
- Permission denied when importing SQL: use a user with CREATE privileges or ask your DBA.

## Extra (optional safety)

- Do not commit real passwords to git. Keep `.env` out of version control.
- For production you should use a secure way to store secrets (not a plain `.env`).
- If `flask` command not found: make sure your virtualenv is activated, or run `python -m flask run` instead.

## Notes & security

- The app uses a random secret key for local testing. For production, set a fixed secret via environment variables and keep it private.
- Do not commit real database passwords to source control. Use environment variables or a secrets manager.

## Next steps (optional improvements)

- Add a `.env` and update the project to read other configuration (e.g., SECRET_KEY) from environment variables.
- Add authentication to protect the UI.
