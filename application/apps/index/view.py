import logging
import asyncio

from flask import jsonify

from application.apps.index import index_blueprint
from application.extensions import redis_cli


@index_blueprint.route("/index")
async def index():
    redis_cli.set('index', 'ok!')
    await asyncio.sleep(1)

    logging.info('请求进入视图！')
    return jsonify(data='welcome flask！'), 200


@index_blueprint.route('/test')
def test():
    try:
        print(1 / 0)
    except Exception as e:
        raise Exception(e)

    return jsonify(data=[]), 200
