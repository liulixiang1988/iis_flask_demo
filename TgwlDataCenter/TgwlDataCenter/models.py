# -*- coding:utf-8 -*-

__author__ = 'Liu Lixiang (liulixiang@gmail.com)'

from . import db


class Fruit(db.Model):
    __tablename__ = 'fruits'
    id = db.Column("id", db.Integer, primary_key=True)
    fruit = db.Column("fruit", db.String(50))

    def __repr__(self):
        return self.fruit