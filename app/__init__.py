
from flask import Flask
from .payments.routes import payments

from config import Config

from flask_cors import CORS

from .models import db, Product
from flask_migrate import Migrate

app = Flask(__name__)

cors = CORS(app, resources={r"/db/<productid>*": {"origins": "*"}})
cors = CORS(app, resources={r"/db*": {"origins": "*"}})
cors = CORS(app, origins=['http://localhost:3000'])


app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

from . import routes 

app.register_blueprint(payments)