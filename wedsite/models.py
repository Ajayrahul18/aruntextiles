from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __str__(self):
        return '<User %r>' % User.id
    
    def is_active(self):
        return True
    
    def is_authenticated(self):
        return True
    
    def get_id(self):
        return str(self.id)



class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    product_picture_zoom = db.Column(db.String(1000), nullable=False)
    product_tag = db.Column(db.String(50), nullable=False)


    def __str__(self):
        return '<Product %r>' % self.product_name
    

class BestSeller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    product_picture_zoom = db.Column(db.String(1000), nullable=False)
    product_tag = db.Column(db.String(50), nullable=False)


    def __str__(self):
        return '<BestSeller %r>' % self.product_name
    
class BestOffers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    product_picture_zoom = db.Column(db.String(1000), nullable=False)
    product_tag = db.Column(db.String(50), nullable=False)


    def __str__(self):
        return '<Product %r>' % self.product_name
    

class Instagram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_picture = db.Column(db.String(1000), nullable=False)



    def __str__(self):
        return '<Product %r>' % self.product_picture
    

class ProductPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    product_picture_zoom = db.Column(db.String(1000), nullable=False)
    product_tag = db.Column(db.String(50), nullable=False)


    def __str__(self):
        return '<Product %r>' % self.product_name
    

