import enum

from sqlalchemy import Column, ForeignKey, types
from sqlalchemy.dialects import postgresql

from application import db


class User(db.Model):
    """Define schema for user table
    """

    id = db.Column(
        db.Integer,
        primary_key=True,
        doc='id do usuário')

    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        index=True,
        default=db.func.now(),
        doc='Data de criação')

    email = db.Column(
        db.String(),
        nullable=False,
        doc='E-mail do usuário')

    name = db.Column(
        db.String(),
        nullable=False,
        doc='Nome do usuário')

    password = db.Column(
        db.String(),
        nullable=False,
        doc='Senha do usuário')
