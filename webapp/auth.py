from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user
from . import views

auth = Blueprint("auth", __name__)


@auth.route("/signin", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        email = request.form.get("InputEmail")
        password = request.form.get("InputPassword")
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user=user, remember=True)
                flash(f"Hey {user.first_name}, you are logged in.", category='success')
            elif not check_password_hash(user.password, password):   
                flash(f"There is a problem with your password...", category='danger') 
            
            
            return render_template("auth/signin.html")
        else:   

            flash(f"Email does not exist, please sign up!", category='danger')
    return render_template("auth/signin.html")


@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("InputEmail")
        first_name = request.form.get("FirstName")
        password1 = request.form.get("InputPassword1")
        password2 = request.form.get("InputPassword2")
        user = User.query.filter_by(email=email).first()
        if user:
            flash("There is already account associated with this email, please log in", category="danger")

        elif len(email) < 6:
            flash("email needs to be greater than 5 characters", category="danger")

        elif len(first_name) < 2:
            flash("First Name needs to be greater than 2 characters", category="danger")
        # elif len(password1) < 9:
        #     flash(
        #         "Your password needs to be greater than 7 characters", category="danger"
        #     )
        elif password1 != password2:
            flash("Looks like your passwords did not match.", category="danger")
        else:
            user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method="sha256"),
            )

            db.session.add(user)
            db.session.commit()
            login_user(user=user, remember=True)
            flash("Account Created!", category="success")
            return redirect(url_for(views.ticktac))
    return render_template("auth/signup.html")


@auth.route("/signout")
@login_required
def sign_out():
    logout_user()
    flash("You have been Signed Out.", category="success")
    return redirect(url_for('views.index'))
