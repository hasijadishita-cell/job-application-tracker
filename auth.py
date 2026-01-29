from werkzeug.security import *
from db import *
import re


def is_valid_email(email):
    if not email:
        return False
    pattern=r"^[\w\.-]+@[\w\.-]+\.(com|net|org|edu|in|au)$"
    return re.match(pattern, email)


def is_valid_password(password):
    return password and len(password)>=8


def create_user(name, email, password):
    con=get_connection()
    cur=con.cursor()

    
    cur.execute("SELECT id FROM users WHERE email=?", (email,))
    if cur.fetchone():
        return False, "Email already registered"
    password= generate_password_hash(password)
    cur.execute("INSERT INTO users (name, email, password) VALUES (?,?,?)", (name, email,password))
    con.commit()
    con.close()
    return True, None

    
        

def authenticate_user(email,password):
    con=get_connection()
    cur=con.cursor()

    cur.execute("SELECT id, name, password FROM users WHERE email=?", (email,))
    user=cur.fetchone()
    con.close()

    if not user:
        return None
    
    if not check_password_hash(user[2], password):
        return None
    
    return{
        "id":user[0],
        "name":user[1]
    }
