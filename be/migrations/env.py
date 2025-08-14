from __future__ import annotations
from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

# --- FLASK IMPORTS ---
from app import create_app, db

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target_metadata to your model's MetaData object
target_metadata = db.metadata


def get_flask_app():
    """Create the Flask app for migrations."""
    # JANGAN simpan app context global / push di level modul
    return create_app()


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    app = get_flask_app()
    with app.app_context():
        url = app.config.get("SQLALCHEMY_DATABASE_URI")
        context.configure(
            url=url,
            target_metadata=target_metadata,
            literal_binds=True,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    app = get_flask_app()
    with app.app_context():
        connectable = db.engine

        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
                compare_type=True,
                compare_server_default=True,
            )

            with context.begin_transaction():
                context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
