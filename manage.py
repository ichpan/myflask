#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_migrate import Migrate

from application import create_app
from application.extensions import db
from application.apps.user.model import User, Role

app = create_app('dev')
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
