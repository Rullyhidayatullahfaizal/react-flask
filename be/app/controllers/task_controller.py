from flask import request, jsonify
from ..models.task_model import Task
from .. import db
from ..utils.response import success_response, error_response


def get_tasks():
    undone = Task.query.filter_by(is_done=False).order_by(Task.created_at.asc()).all()
    done = Task.query.filter_by(is_done=True).order_by(Task.created_at.desc()).all()
    return success_response({
        "undone": [task_to_dict(t) for t in undone],
        "done": [task_to_dict(t) for t in done]
    }, "Tasks fetched successfully")



def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return error_response("Title is required", 400)

    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return success_response(task_to_dict(new_task), "Task created successfully", 201)

def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    if not data or 'title' not in data:
        return error_response("Title is required", 400)

    task.title = data['title']
    db.session.commit()
    return success_response(task_to_dict(task), "Task updated successfully")


def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return success_response(None, "Task deleted successfully", 204)


def mark_done(task_id):
    task = Task.query.get_or_404(task_id)
    task.is_done = True
    db.session.commit()
    return success_response(task_to_dict(task), "Task marked as done")


def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "is_done": task.is_done,
        "created_at": task.created_at.isoformat()
    }
