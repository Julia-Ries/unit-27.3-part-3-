"""Models for Blogly."""

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"



class User(db.Model):
    """blog site user"""


    __tablename__ = "users"

    id = db.Column(db.Integer, 
                    primary_key = True,
                    autoincrement= True)
    first_name = db.Column(db.Text,
                            nullable =False)
    last_name = db.Column(db.Text,
                        nullable=False)
    image_url = db.Column(db.Text, 
                        nullable=False, default= DEFAULT_IMAGE_URL)


    posts = db.relationship("Post", backref= "user")

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"


class Post(db.Model):
    """blog post"""

    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default= datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)


    
class Tag(db.Model):
    """tag on a post"""

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False, unique = True)

    posts = db.relationship("Post", secondary = "posts_tags", backref = "tags")



class PostTag(db.Model):
    """joins together a Post and a Tag"""

    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key = True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key = True)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)



