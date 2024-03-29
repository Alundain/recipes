from flask import Flask, render_template, redirect,request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')

#encriptar contraseña
    pass_encrypt = bcrypt.generate_password_hash(request.form['password'])
    form = {
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "email":request.form['email'],
        "password": pass_encrypt
    }
    new_id = User.save(form)
    session['user_id'] = new_id
    return redirect('/dashboard') # acá cambiar por las recetas

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect("/")
    form = {'id': session['user_id']}
    user = User.get_by_id(form)
    recipes=Recipe.get_my_recipes(form)
    other_recipes = Recipe.get_others_recipes(form)
    return render_template("dashboard.html", user=user,recipes=recipes, other_recipes=other_recipes)

@app.route("/login", methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Email no registrado", "login")
        return redirect("/")
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Password incorrecto", "login")
        return redirect("/")
    session['user_id'] = user.id
    return redirect("/dashboard")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")