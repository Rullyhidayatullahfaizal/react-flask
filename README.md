🚀 Getting Started
1) Clone & Enter the Project Directory
git clone <REPO_URL>
cd <project-folder>

2) Create Virtual Environment & Install Dependencies

Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt


macOS/Linux:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


If you don’t have requirements.txt, install the essentials:

pip install flask flask-cors flask-sqlalchemy psycopg2-binary flask-migrate python-dotenv

3) Create the PostgreSQL Database

Make sure PostgreSQL is running.

Using psql (example DB name: todo_db):

CREATE DATABASE todo_db;


Or create it via a GUI tool like pgAdmin or DBeaver.

4) Create .env File

Create a .env file in the project root (same level as run.py):

FLASK_APP=run
FLASK_ENV=development
DATABASE_URL=postgresql://postgres:admin123@localhost:5432/todo_db


Note: Some environments require the prefix postgresql:// instead of postgres://.

5) Initialize & Run Migrations

Make sure the virtual environment is active when running these commands.

flask db init            # only needed the first time if migrations folder doesn't exist
flask db migrate -m "initial schema"
flask db upgrade


If successful, users and todos tables will be created in your database.

6) Seed Users

The project includes a CLI command to seed default users (Admin, Rully, Guest):

flask seed-users


The output will display the user IDs. Use these user_id values when creating ToDos.

7) Start the Server
flask run
# or
python run.py


By default, it runs on: http://localhost:5000

Common Issues & Quick Fixes

flask: command not found / 'flask' is not recognized
→ The virtual environment is not active. Activate it first:

Windows: .\venv\Scripts\Activate

macOS/Linux: source venv/bin/activate

No module named flask_migrate
→ Install: pip install flask-migrate

ForeignKeyViolation (user_id) when POSTing /todos
→ Run: flask seed-users and use a valid user_id.

Migrations succeed but tables don’t appear
→ In migrations/env.py, ensure target_metadata = db.metadata and app context is created inside the migration functions; also ensure from app import models is in app/__init__.py after db.init_app(app).

