from flask import Blueprint, render_template, flash, redirect, request, jsonify
from .models import Product,BestOffers,Instagram, BestSeller, ProductPage, Cart
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)

API_PUBLISHABLE_KEY = 'YOUR_PUBLISHABLE_KEY'

API_TOKEN = 'YOUR_API_TOKEN'


@views.route('/')
def index():
    items = Product.query.all()
    items_bestSeller = BestSeller.query.all()
    items_bestOffer = BestOffers.query.all()
    items_insta = Instagram.query.all()
    items_product = ProductPage.query.all()
    return render_template("index.html", items = items, 
                           items_bestSeller=items_bestSeller, 
                           items_bestOffer=items_bestOffer, 
                           items_insta = items_insta, 
                           items_product=items_product)


@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/productPage", methods=['GET'])
def productPageList():
    items = ProductPage.query.all()
    return render_template("productPage.html", items = items)


@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/adminLoginPage")
def adminLoginPage():
    return render_template("adminLoginPage.html")

# @views.route("/cart", endpoint='cart')
# @login_required
# def showCart():
#     cart_items = Cart.query.filter_by(customer_link=current_user.id).all()
#     total_amount = sum(item.productpage.current_price * item.quantity for item in cart_items)
#     csrf_form = CSRFProtectionForm()  # Create an instance of the CSRF form
#     return render_template("cart.html", cart_items=cart_items, total_amount=total_amount, form=csrf_form)


