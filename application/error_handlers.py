#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from flask import jsonify


def exception_404_not_found(error):
    logging.error("An exception occurred: {}".format(str(error)))
    return '404 not found.', 404


def exception_method_not_allow(error):
    logging.error("An exception occurred: {}".format(str(error)))
    return 'method not allowed', 405


def exception_internal_server_error(error):
    logging.error("An exception occurred: {}".format(str(error)))
    return jsonify(msg='call interface successfully', status_code=5000), 500
