from flask import Blueprint, render_template, session, redirect, request, url_for
from .models import Admin
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__, url_prefix='/aruntextiles')


@auth.route("/userLogin", methods=["GET", "POST"])
def userLogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Admin.query.filter_by(username=username).first()
        

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        else:
            return render_template('userLogin.html', error='Invalid credentials')

    return render_template("userLogin.html")



@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.userLogin'))

@auth.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

