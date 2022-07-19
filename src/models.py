import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=True)
    email = Column(String(250), nullable=False)
    Follows = relationship("Follower")

    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id = relationship(User)

    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_id_rel = relationship(User, primaryjoin=user_from_id == User.id)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_to_rel = relationship(User, primaryjoin=user_to_id == User.id)

    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type_of = Column(Enum())
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post, primaryjoin=post_id == Post.id)

    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(400))
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post, primaryjoin=post_id == Post.id)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')