from task_lectures.lectures.viewer import ns as lectures
from task_lectures.lectures import api
from flask import Flask, Blueprint
from flask_cors import CORS

app = Flask(__name__)
blueprint = Blueprint('api', __name__)

api.init_app(blueprint)
api.add_namespace(lectures, '/lectures')
app.register_blueprint(blueprint)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


if __name__ == "__main__":
    host = '0.0.0.0'
    port = '5000'
    debug = True
    app.run(host, int(port), debug)