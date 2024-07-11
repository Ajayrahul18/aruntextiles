from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __str__(self):
        return '<Admin %r>' % Admin.id
    
    def is_active(self):
        return True
    
    def is_authenticated(self):
        return True
    
    def get_id(self):
        return str(self.id)
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    lastname = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(100), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)

    cart_items = db.relationship('Cart', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

    def __repr__(self):
        return f'<User  {self.id}>' 



class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    product_picture_zoom = db.Column(db.String(1000), nullable=False)
    product_tag = db.Column(db.String(50), nullable=False)


    def __str__(self):
        return f'<Product {self.product_name}>' 
    

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
    

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    user_link = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_link = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __str__(self):
        return f'<Cart {self.id}>' 


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    payment_id = db.Column(db.String(50), nullable=False)

    user_link = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_link = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __str__(self):
        return '<Order %r>' % self.id