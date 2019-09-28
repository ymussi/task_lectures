from flask_restplus import fields
from task_lectures.lectures import api


schemaLecture = api.model('Lectures', {
    'data': fields.List(fields.String)
})