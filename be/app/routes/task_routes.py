from flask import Blueprint
from flask_cors import CORS
from ..controllers import task_controller

task_bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")
CORS(task_bp, origins=["http://localhost:5173"])

@task_bp.route("", methods=["GET"])
def get_tasks():
    return task_controller.get_tasks()

@task_bp.route("", methods=["POST"])
def create_task():
    return task_controller.create_task()

@task_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    return task_controller.update_task(task_id)

@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    return task_controller.delete_task(task_id)

@task_bp.route("/done/<int:task_id>", methods=["PATCH"])
def mark_done(task_id):
    return task_controller.mark_done(task_id)
