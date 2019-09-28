from flask_restplus import Resource
from flask import request, jsonify
from task_lectures.lectures import api
from task_lectures.lectures.schemas import schemaLecture
from task_lectures.lectures.controller import Lecture
import logging
import json


log = logging.getLogger(__name__)

ns = api.namespace(
    'lectures', description='')


@ns.route('/lecture')
class Create(Resource):
    @ns.response(code=400, description="Bad Request")
    @ns.expect(schemaLecture, validate=True)
    def post(self):
        """
        Faz um cadastro simples na base de dados
        """
        dados = request.json
        r = Lecture(dados)
        res = r.set_tracks()

        return res