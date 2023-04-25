import logging

from flask import jsonify

from application.apps.index import index_blueprint
from application.extensions import redis_cli


@index_blueprint.route("/")
def index():
    redis_cli.set('index', 'ok!')
    logging.info('请求进入视图！')
    return jsonify(data='welcome flask！'), 200
