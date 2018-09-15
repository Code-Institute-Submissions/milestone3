import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Check wether username given is blank, already taken or valid
def verify_username(username):
    if username == "":
        return "noUser"
        
    # open users_test.txt and check wether the username is already taken
    with open("data/users.txt", "r") as file:
        users = file.read().splitlines()
        
    for user in users:
        if user == username:
            return "notUnique"
    return True

#Takes username as an input value
def add_username():
    username = request.form["username"]
    
    # If username is verified
    if verify_username(username) == "noUser":
      return "noUser"
    elif verify_username(username) == "notUnique":
      return "notUnique"
    else:
      with open("data/users.txt", "a") as file:
        file.write(username + "\n")
        file.close()
      return username


@app.route('/' , methods=["GET", "POST"])
def index():
    userText = "Enter A Username To Begin"
    if request.method == "POST":
        user = add_username()
        if user == "noUser":
          userText = "Oops! Please Enter A Username To Begin"
        elif user == "notUnique":
          userText = "Oops! That Username Is Already Taken"
        else:
          return redirect("/questions/" + request.form["username"])
    return render_template("index.html", user=userText)

@app.route('/questions/<username>')
def questions(username):
    return render_template("questions.html", username=username)    
    
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