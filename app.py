from flask import Flask
from flask_migrate import Migrate
from models.Models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost:3306/welshacademy?user=root'

# Initialize plugins
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
