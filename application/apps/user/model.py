#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_method

from application.extensions import db


class User(db.Model):
    __tablename__ = 't_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, comment='用户名')
    password = db.Column(db.String(256), nullable=False, comment='密码')
    role = db.Column(db.Integer, nullable=True, comment='角色')
    is_admin = db.Column(db.Boolean, default=False)
    mobile = db.Column(db.String(16), nullable=True, comment='手机号')
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    @hybrid_method
    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'role': self.role,
            'is_admin': self.is_admin,
            'mobile': self.mobile,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }


class Role(db.Model):
    __tablename__ = 't_role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, comment='角色名')
    uid = db.Column(db.Integer, db.ForeignKey('t_user.id'), comment='用戶id')
    t_user = db.relationship("User", foreign_keys=uid)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return '<Role %r>' % self.name

    @hybrid_method
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'uid': self.uid,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }
