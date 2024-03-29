from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re # expresiones regulares para validar
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # expresion regular email

class User: 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
    
    @staticmethod
    def validate_user(data):
        is_valid = True
        
        # validar nombre
        if len(data['first_name']) < 2 :
            flash("El nombre del usuario debe tener al menos dos caracteres", "register")
        
        #validar apellido
        if len(data['last_name']) < 2 :
            flash("El Apellido del usuario debe contener al menos 2 caracteres", "register")
        
        #validar password tenga al menos 6 caracteres
        if len(data['password']) < 6:
            flash('Contraseña debe contener al menos 6 caracteres', 'register')
            is_valid = False
        
        #verificar que las contraseñas coincidan
        if data['password'] != data['confirm']:
            flash('Las contraseñas no coinciden', 'register')  
            is_valid = False

        #patron correcto del correo electronico
        if not EMAIL_REGEX.match(data['email']):
            flash("Email ingresado no es válido", "register")
            is_valid = False
        
        #consultar si existe el correo electronico
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('esquema_recipes').query_db(query,data)
        if len(results) >= 1:
            flash("Email registrado previamente", "register")
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, password) VALUES( %(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('esquema_recipes').query_db(query, data)
        return result
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('esquema_recipes').query_db(query, data)
        if len(results) == 1:
            user = cls(results[0])
            return user
        else:
            return False
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('esquema_recipes').query_db(query,data)
        user = cls(results[0])
        return user                