#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from flask import jsonify


def exception_404_not_found(error):
    logging.error("An exception occurred: {}".format(str(error)))
    return jsonify(msg='404 not found.'), 404


def exception_method_not_allow(error):
    logging.error("An exception occurred: {}".format(str(error)))
    return jsonify(msg='method not allowed'), 405
