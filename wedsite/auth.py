from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from .models import Admin, User
from flask_login import login_user, login_required, logout_user, current_user
from .forms import UserSigupForm, UserLoginForm, UserProfileUpdateForm
from werkzeug.security import generate_password_hash
from .import db

auth = Blueprint('auth', __name__, url_prefix='/aruntextiles')


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
        form.birthday.data = current_user.birthday

    return render_template('customer_profile_update.html', form=form)


@auth.route("/adminLogin", methods=["GET", "POST"])
def adminLogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Admin.query.filter_by(username=username).first()
        

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        else:
            return render_template('admin.html', error='Invalid credentials')

    return render_template("admin.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.adminLogin'))

@auth.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

