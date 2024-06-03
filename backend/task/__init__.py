from flask import Blueprint, request, jsonify
from .models import Task, TaskSchema
from config import db
from utils import to_datetime
from typing import Sequence
import http

task_blueprint = Blueprint('task', __name__)

@task_blueprint.route('/')
def get_tasks():
    tasks: Sequence[Task] = db.session.execute(db.select(Task)).scalars().all()
    ts = TaskSchema(many = True)
    
    
    return ts.dumps(tasks)

@task_blueprint.get('/<int:tid>')
def get_task(tid):
    task = db.session.execute(db.select(Task).where(Task.id == tid)).scalar()
    
    if task is None:
        return jsonify("Error!"), http.HTTPStatus.BAD_REQUEST
    
    return TaskSchema().dump(task)

@task_blueprint.post('/add')
def add_task():
    task_json = request.get_json()
    
    task = Task(title=task_json['title'], description=task_json['description'], due=to_datetime(task_json['due']))
    
    db.session.add(task)
    db.session.commit()
    
    ts = TaskSchema()
    
    return ts.dump(task)

@task_blueprint.delete('/remove/<int:tid>')
def delete_task(tid):
    task = db.session.execute(db.select(Task).where(Task.id == tid)).scalar()
    if task is None:
        return jsonify("Error!"), http.HTTPStatus.BAD_REQUEST
    
    db.session.delete(task)
    db.session.commit()
    
    ts = TaskSchema()
    return ts.dump(task)

@task_blueprint.put('/edit')
def edit_task():
    new_task = request.get_json()
    
    old_task = db.session.execute(db.select(Task).where(Task.id == new_task['id'])).scalar()
    
    if old_task is None:
        return jsonify("Error!"), http.HTTPStatus.BAD_REQUEST
    
    old_task.title = new_task['title']
    old_task.description = new_task['description']
    old_task.due = to_datetime(new_task['due'])
    old_task.complete = new_task['complete']
    
    db.session.commit()
    
    return TaskSchema().dump(old_task)