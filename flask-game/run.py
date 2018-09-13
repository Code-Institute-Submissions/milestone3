import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/about')
def about():
    return render_template("about.html")
    
@app.route('/instructions')
def instructions():
    return render_template("instructions.html")
    
@app.route('/contact')
def contact():
    return render_template("contact.html")
    

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)