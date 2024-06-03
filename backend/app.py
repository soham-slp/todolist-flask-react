from config import app, db
from flask_migrate import Migrate
from task import task_blueprint

Migrate(app, db)
app.register_blueprint(task_blueprint, url_prefix='/task')