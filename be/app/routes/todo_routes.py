from flask import Blueprint, request
from flask_cors import CORS
from app.controllers import todo_controller

todo_bp = Blueprint("todo_bp", __name__, url_prefix="/todos")
CORS(todo_bp, origins=["http://localhost:5173"])


@todo_bp.route("/", methods=["GET"])
def get_todos():
    return todo_controller.get_all_todos()

@todo_bp.route("/", methods=["POST"])
def add_todo():
    data = request.get_json()
    return todo_controller.create_todo(data)

@todo_bp.route("/<int:todo_id>", methods=["DELETE"])
def remove_todo(todo_id):
    return todo_controller.delete_todo(todo_id)
