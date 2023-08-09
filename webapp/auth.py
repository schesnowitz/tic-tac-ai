from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route("/signin")
def sign_in():
    return render_template("/auth/signin.html")


@auth.route("/signup")  
def sign_up():
    return render_template("/auth/signup.html")


@auth.route("/signout") 
def sign_out():
    return render_template("auth/signout.html")