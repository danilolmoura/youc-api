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


class Channel(db.Model):
    """Define schema for channel table
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

    name = db.Column(
        db.String(),
        nullable=False,
        doc='Nome do canal')

    url = db.Column(
        db.String(),
        nullable=False,
        doc='url do canal')


class Video(db.Model):
    """Define schema for video table
    """

    id = db.Column(
        db.Integer,
        primary_key=True,
        doc='id do usuário')

    channel_id = db.Column(
        db.Integer,
        db.ForeignKey('channel.id'),
        nullable=False,
        doc='Id do canal')

    channel = db.relationship('Channel')

    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        index=True,
        default=db.func.now(),
        doc='Data de criação')

    description = db.Column(
        db.String(),
        nullable=False,
        default='',
        doc='Descrição do vídeo')

    duration = db.Column(
        db.Integer(),
        nullable=False,
        doc='Duração do vídeo')

    title = db.Column(
        db.String(),
        nullable=False,
        doc='Título do vídeo')

    image_urls = db.Column(
        db.ARRAY(db.String()),
        nullable=False,
        default=[],
        doc='URL de imagens do vídeo')

    url = db.Column(
        db.String(),
        nullable=False,
        doc='URL do vídeo')

    video_rate = db.Column(
        db.Integer(),
        nullable=False,
        doc='Nota do vídeo')

    views_count = db.Column(
        db.Integer(),
        nullable=False,
        doc='Quantidade de views')
