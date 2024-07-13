from flask import Blueprint, render_template, session, redirect, request, url_for, flash, jsonify
from .models import Admin, User, ProductPage, Cart
from flask_login import login_user, login_required, logout_user, current_user
from .forms import UserSigupForm, UserLoginForm, UserProfileUpdateForm, AdminLoginForm, DummyForm

from werkzeug.security import generate_password_hash
from .import db

auth = Blueprint('auth', __name__, url_prefix='/aruntextiles')



@auth.route('/remove_from_cart/<int:cart_item_id>', methods=['POST'])
@login_required
def remove_from_cart(cart_item_id):
    cart_item = Cart.query.get(cart_item_id)
    db.session.delete(cart_item)
    db.session.commit()
    return redirect(url_for('auth.cart'))


@auth.route('/check_login_status', methods=['GET'])
def check_login_status():
    is_logged_in = current_user.is_authenticated
    return jsonify({'is_logged_in': is_logged_in})


@auth.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    data = request.get_json()
    quantity = data.get('quantity', 1)
    product = ProductPage.query.get_or_404(product_id)
    cart_item = Cart.query.filter_by(user_link=current_user.id, product_link=product_id).first()
    
    if cart_item:
        cart_item.quantity += quantity
        current_quantity = cart_item.quantity
    else:
        new_cart_item = Cart(user_link=current_user.id, product_link=product_id, quantity=quantity)
        db.session.add(new_cart_item)
        current_quantity = new_cart_item.quantity
    
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Product added to cart successfully!', 'quantity': current_quantity})

@auth.route('/cart')
@login_required
def cart():
    cart_items = Cart.query.filter_by(user_link=current_user.id).all()
    
    cart_details = []  # To hold cart items with product details
    total_amount = 0
    
    for item in cart_items:
        product = ProductPage.query.get(item.product_link)  # Fetch the ProductPage object
        if product:  # Check if product exists
            cart_details.append({
                'cart_item': item,
                'product': product
            })
            total_amount += product.current_price * item.quantity
    
    return render_template('cart.html', cart_details=cart_details, total_amount=total_amount)


@auth.route("/userSignUp", methods=["GET", "POST"])
def userSignUp():
    form = UserSigupForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.user_name.data
        password_1 = form.password_1.data
        password_2 = form.password_2.data

        print(f"Received form data: email={email}, username={username}, password1={password_1}, password2={password_2}")

        if password_1 == password_2:
            new_customer = User(
                email=email,
                username=username,
                password_hash=generate_password_hash(password_2)
            )


            try:
                db.session.add(new_customer)
                db.session.commit()
                flash('Account Created Successfully, You can now Login')
                print('Account Created Successfully, You can now Login')
                return redirect(url_for('auth.adminLogin'))
            except Exception as e:
                print(f"Exception occurred: {e}")
                flash('Account not Created, Email already exists')
                print('Account not Created, Email already exists')

        else:
            flash('Passwords do not match')
            print('Passwords do not match')

    print("Form validation failed or method is GET")
    return render_template("userSignupForm.html", form=form)



@auth.route("/userLogin", methods=["GET", "POST"])
def userLogin():
    form = UserLoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash('User Login Successful:'+ user.username)
            return redirect(url_for('auth.userProfile', user_id=user.id))

        else:
            flash('Invalid credentials')
            return render_template('userLogin.html', form=form, error='Invalid credentials')
    return render_template("userLogin.html", form=form)

@auth.route("/userProfile/<int:user_id>")
def userProfile(user_id):
    customer = User.query.get(user_id)
    return render_template("userProfile.html", customer=customer)

@auth.route("/UserProfileUpdate", methods=["GET", "POST"])
def UserProfileUpdate():
    form = UserProfileUpdateForm()
    if form.validate_on_submit():
        customer = User.query.get(current_user.id)
        customer.firstname = form.firstname.data
        customer.email = form.email.data
        customer.phone = form.phone.data
        customer.address = form.address.data

        db.session.commit()
        return redirect(url_for('auth.UserProfileUpdate'))
    
    elif request.method == 'GET':
        form.firstname.data = current_user.firstname
        form.email.data = current_user.email
        form.phone.data = current_user.phone
        form.address.data = current_user.address

    return render_template('customer_profile_update.html', form=form)


@auth.route("/adminLogin", methods=["GET", "POST"])
def adminLogin():
    form = AdminLoginForm()
    print("Form created:", form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = Admin.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        else:
            # Optionally handle failed login
            flash("Invalid username or password", "danger")

    return render_template("adminLoginPage.html", form=form)



@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("index.html")

@auth.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

