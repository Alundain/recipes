from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe: 
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.descriptions = data['descriptions']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        #join con nombre
        self.first_name = data['user_id']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes(name, description, instructions, date_made, under_30, user_id) VALUES(%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, %(user_id)s )"
        results = connectToMySQL('esquema_recipes').query_db(query,data)
        return results
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data['name']) < 3:
            flash('El nombre de la receta debe al menos 3 caracteres', 'recipe')
            is_valid = False
        if len(data['description']) < 3:
            flash('La descripción de la receta es demasiado corta, debe contener más de 3 caracteres', 'recipe')
            is_valid = False
        if len(data['instructions']) < 3:
            flash('Las instrucciones de la receta es demasiado corta, debe contener más de 3 caracteres', 'recipe')
        if len(data['date_made']) < 3:
            flash('Ingrese una fecha', 'recipe')
        return is_valid
    
    @classmethod
    def get_all(cls):
        query = "SELECT recipes.*, first_name FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL('esquema_recipes').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
