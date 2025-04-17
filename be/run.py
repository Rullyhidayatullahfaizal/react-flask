from app import create_app, db
from flask.cli import with_appcontext
import click
from app.utils.response import error_response


app = create_app()

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

# 👇 Hanya jika kamu run langsung file ini
if __name__ == "__main__":
    app.run(debug=True)