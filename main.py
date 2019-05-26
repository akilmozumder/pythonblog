from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/cleanblog'
db = SQLAlchemy(app)

class tbl_contact(db.Model):
   
    Id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    mobile_no=db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(120), nullable=False)

@app.route("/")
def home():
    
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/contact",methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = tbl_contact(name=name, email = email, mobile_no = phone, message=message)
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html")

app.run(debug=True)