import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True) #El primary_key me ayuda a IDENTIFICAR de manaera equivoca al personaje, planeta, user.
    username = Column(String(100))
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(100))
    children_post = relationship("Post")
    children_follower = relationship("Follower")
    children_comment = relationship("Comment")
    children_follower2 = relationship("Follower")
    

    


class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id')) #Cual seria el nombre adecuado?
    children_media = relationship ("Media")
    children_comment = relationship("Comment")


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer,primary_key=True)
    tipo = Column(String(100)) 
    url = Column(String(100))
    post_id = Column(Integer,ForeignKey('post.id'))
    
    


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500))
    author_id = Column(Integer, ForeignKey('user.id')) #DUDA NOMBRE, no seria user id?
    post_id = Column(Integer,ForeignKey('post.id'))

class Follower(Base): #
    __tablename__= 'follower' 
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
     













    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')