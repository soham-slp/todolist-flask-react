from config import ma
from .task import Task
from marshmallow import fields

class TaskSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Task
    
    id = ma.auto_field()
    title = ma.auto_field()
    description = ma.auto_field()
    due = fields.DateTime('iso')
    complete = ma.auto_field()
    