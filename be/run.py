from re import M
from app import create_app, db
from flask.cli import with_appcontext
import click
from app.utils.response import error_response
from flask_migrate import Migrate
from app.models.user import User




app = create_app()
migrate = Migrate(app, db) 

@app.cli.command("init-db")
@with_appcontext
def init_db():
    db.create_all()
    click.echo("Database initialized.")

@app.errorhandler(404)
def not_found(e):
    print(f"[404 ERROR] {e}")
    return error_response("Resource not found", 404)

@app.errorhandler(405)
def method_not_allowed(e):
    print(f"[405 ERROR] {e}")
    return error_response("Method not allowed", 405)

@app.errorhandler(500)
def internal_error(e):
    print(f"[500 ERROR] {e}")
    return error_response("Internal server error", 500)

@app.cli.command("seed-user")
@with_appcontext
def seed_users():
    users_to_seed = [
        {"name": "Admin", "email": "admin@example.com"},
        {"name": "Rully", "email": "rully@example.com"},
        {"name": "Guest", "email": "guest@example.com"}
    ]

    for udata in users_to_seed:
        existing = User.query.filter_by(name=udata["name"]).first()
        if not existing:
            user = User(name=udata["name"], email=udata["email"])
            db.session.add(user)
            click.echo(f"User '{udata['name']}' will be created")
        else:
            click.echo(f"User '{udata['name']}' already exists with id={existing.id}")

    db.session.commit()
    click.echo("Seeding complete ✅")

# 👇 Hanya jika kamu run langsung file ini
if __name__ == "__main__":
    app.run(debug=True)