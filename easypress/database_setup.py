#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Theme(Base):
    __tablename__ = 'theme'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    meta_id = Column(String(500))
    meta_key = Column(String(500))
    meta_value = Column(String(500))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'title': self.post_title,
            'meta_id': self.post_author,
            'meta_key': self.url,
            'meta_value': self.url,
        }


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user = Column(String(250), nullable=False)
    image = Column(String(500), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250))
    theme_id = Column(Integer, ForeignKey('theme.id'))
    theme = relationship(Theme)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'email': self.email,
            'image': self.image,
            'theme_id': self.theme_id
        }



class Page(Base):
    __tablename__ = 'page'

    id = Column(Integer, primary_key=True)
    page_title = Column(String(300))
    url = Column(String(500))
    edit_url = Column(String(500))
    thumbnail = Column(String(500))
    publish_date = Column(String(300))
    published = Column(String(30))
    hidden = Column(String(3))
    like = Column(Integer)
    dislike = Column(Integer)
    theme_id = Column(Integer, ForeignKey('theme.id'))
    theme = relationship(Theme)
    page_creator = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'page_title': self.page_title,
            'url': self.url,
            'edit_url': self.url,
            'thumbnail': self.thumbnail,
            'publish_date': self.post_date,
            'published': self.post_content,
            'published': self.published,
            'hidden': self.hidden,
            'like': self.like,
            'dislike': self.dislike,
            'theme_id': self.theme_id,
            'page_creator': self.page_creator

        }


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    post_title = Column(String(300))
    url = Column(String(500))
    edit_url = Column(String(500))
    thumbnail = Column(String(500))
    post_date = Column(String(300))
    post_content = Column(String())
    published = Column(String(30))
    hidden = Column(String(3))
    like = Column(Integer)
    dislike = Column(Integer)
    post_author = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    page_id = Column(Integer, ForeignKey('page.id'))
    page = relationship(Page)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'post_title': self.post_title,
            'post_author': self.post_author,
            'url': self.url,
            'edit_url': self.url,
            'thumbnail': self.thumbnail,
            'post_date': self.post_date,
            'post_content': self.post_content,
            'published': self.published,
            'hidden': self.hidden,
            'like': self.like,
            'dislike': self.dislike,
            'theme_id': self.theme_id
        }






engine = create_engine('sqlite:///easypress.db')
Base.metadata.create_all(engine)
