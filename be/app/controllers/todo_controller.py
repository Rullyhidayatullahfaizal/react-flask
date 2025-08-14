from app import db
from app.models.todo import ToDo
from flask import jsonify

from app.models.user import User

def get_all_todos():
    todos = ToDo.query.all()
    return jsonify([{
        "id": todo.id,
        "name": todo.name,
        "is_active": todo.is_active,
        "user_id": todo.user_id,
        "created_at": todo.created_at,
        "updated_at": todo.updated_at
    } for todo in todos]), 200

def create_todo(data):
    try:
        name = (data.get("name") or "").strip()
        user_id = data.get("user_id")

        if not name:
            return jsonify({"error": "Name is required and cannot be empty"}), 400
        if user_id is None:
            return jsonify({"error": "User ID is required"}), 400
        if not isinstance(user_id, int):
            return jsonify({"error": "User ID must be an integer"}), 400
        if not User.query.get(user_id):
            return jsonify({"error": f"User with id={user_id} not found"}), 400

        todo = ToDo(name=name, user_id=user_id)
        db.session.add(todo)
        db.session.commit()

        return jsonify({
            "message": "ToDo created",
            "data": {
                "id": todo.id,
                "name": todo.name,
                "is_active": todo.is_active,
                "user_id": todo.user_id,
                "created_at": todo.created_at.isoformat() if todo.created_at else None,
                "updated_at": todo.updated_at.isoformat() if todo.updated_at else None,
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    

def delete_todo(todo_id):
    todo = ToDo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "ToDo not found"}), 404

    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "ToDo deleted successfully"}), 200