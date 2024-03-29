from flask import render_template, redirect, session, request
from flask_app import app

#models user y recipe
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/new/recipe')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    
    receta = {"id" : session['user_id']}

    user = User.get_by_id(receta)
    return render_template('new_recipe.html', user=user)

@app.route('/create/recipe', methods=['POST'])
def create_recipe():
    if 'user_id' not in session: #acá comprobamos inicio de sesión
        return redirect('/')
    
    #validación de receta
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')

#guardar receta
    Recipe.save(request.form)
    return redirect('/dashboard')

@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    
    receta = {"id":session['user_id']}
    user = User.get_by_id(receta)
    form_receta = {"id": id}
    receta = User.get_by_id(form_receta)
    return render_template('edit_recipe.html', user=user, receta=receta)

@app.route("/update", methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect("/")
    # recibimos el request form
    # validar que la info de recetas sea correcta
    if not Recipe.validate_recipe(request.form):
        return redirect("/edit/"+request.form['id'])
    Recipe.update(request.form)
    return redirect("/dashboard")

@app.route("/delete/<int:id>")
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect("/")
    data_receta = {"id":id}
    #metod que elimine un registro en base a la id
    Recipe.delete(data_receta)
    return redirect()