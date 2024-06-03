from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
import yaml
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

with open('config.yaml') as f:
    cfg = yaml.load(f, yaml.FullLoader)

app = Flask(__name__)
CORS(app)
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = cfg['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = cfg['SQLALCHEMY_TRACK_MODIFICATIONS']

db = SQLAlchemy(app, model_class=Base)
