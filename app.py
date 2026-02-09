from db import *
from flask import *
from auth import *
import os

app=Flask(__name__)
app.secret_key=os.environ.get("SECRET_KEY")

@app.route("/")
def home():
    return redirect("/signup")
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")

        if not is_valid_email(email):
            flash("Enter a valid email address")
            return redirect("/signup")
        
        if not is_valid_password(password):
            flash("Password must be at least 8 characters")
            return redirect("/signup")
        

        success,error=create_user(name, email, password)
        

        if not success:
            flash(error)
            return redirect("/signup")
        
        return redirect("/login")
    
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        if not email or not password:
            flash("Email and password required")
            return redirect("/login")
        user=authenticate_user(email,password)

        if not user:
            flash("Invalid email or password")
            return redirect("/login")
        
        session["user_id"]=user["id"]
        session["user_name"]=user["name"]
        return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    
    user_id=session["user_id"]
    filter_status=request.args.get("status") or "all"
    selected_month=request.args.get("month") or "all"
    application=get_data(user_id,filter_status,selected_month)
    print(application)
    
    
    return render_template("dashboard.html", name=session["user_name"], application=application)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/add-application", methods=["GET", "POST"])
def add_application_route():
    if "user_id" not in session:
        return redirect ("/login")
    
    if request.method=="POST":
        company=request.form.get("company")
        role=request.form.get("role")
        status=request.form.get("status")
        applied_date=request.form.get("applied_date")
        user_id=session["user_id"]

        add_application(user_id,company,role,status,applied_date)

        return redirect("/dashboard")
    
    return render_template("add_application.html")

@app.route("/delete-application/<int:app_id>", methods=["POST"])
def delete_application_route(app_id):
    if "user_id" not in session:
        return redirect ("/login")
    
    delete_application(app_id, session["user_id"])
    return redirect("/dashboard")




@app.route("/edit/<int:app_id>", methods=["GET"])
def edit_application_route(app_id):
    if "user_id" not in session:
        return redirect ("/login")
    user_id=session["user_id"]
    app=edit_application(app_id,user_id)

    if app is None:
        return "Unauthorized",403
    
    return render_template("edit.html",app=app)


@app.route("/update/<int:app_id>", methods=["POST"])
def update(app_id):
    if "user_id" not in session:
        return redirect ("/login")
     
    company=request.form.get("company")
    role=request.form.get("role")
    status=request.form.get("status")
    applied_date=request.form.get("applied_date")

    update_application(company,role,status,applied_date,app_id,session["user_id"])
    flash("Application updated successfully!", "success")
    
    return redirect("/dashboard")


    

if __name__=="__main__":
    init_db()
    app.run(debug=True)