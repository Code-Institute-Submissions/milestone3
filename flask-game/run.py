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
      
#Gets Questions from questions.txt
def get_questions():
    questions = []
    answers = []
    
    # reads questions_test.txt and splits even lines into questions and odd lines into answers
    with open("data/questions.txt", "r") as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    return questions, answers
    
    
# Checks Wether guess is correct, inncorect or is a pass
def check_guess(answer, guess, lives, question_num, questions_score, passed_on, username):
  
  status = ""
  def url(status):
    return redirect("/questions/" + status + "/" + question_num + "/" + questions_score + "/" + passed_on + "/" + lives + "/" + guess + "/" + username)
 
  if( guess == answer ):
    status = "correct"
    return url(status)
  elif ( guess == "pass" ):
    status = "pass"
    return url(status)
  else:
    status = "wrong"
    return url(status)


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
          return redirect("/questions/0/1/0/0/5/0/" + request.form["username"])
    return render_template("index.html", user=userText)
    


@app.route('/questions/<status>/<question_num>/<questions_score>/<passed_on>/<lives>/<guess>/<username>', methods=["GET", "POST"])
def questions(status, question_num, questions_score, passed_on, lives, guess, username):
  questions = get_questions()
  q_num = int(question_num) - 1
  question = questions[0][q_num]
  answer = questions[1][q_num]
  message = ""
  bg =""
  
  if ( status == "wrong" ):
    message = "'{0}', Was Incorrect".format(guess)
    lives = str(int(lives) - 1)
    bg = "#FF4D4C"
    
    
  
  if request.method == "POST":
    guess = request.form["answer"]
    
    url = check_guess(answer, guess, lives, question_num, questions_score, passed_on, username)
    
    return url
    
  return render_template(
    "questions.html",
    message=message,
    question=question,
    lives=lives,
    questionNum=question_num,
    questionsScore=questions_score,
    passed=passed_on,
    bg=bg,
    username=username
    ) 
    


# @app.route('/questions/wrong/<question_num>/<questions_score>/<passed_on>/<lives>/<guess>/<username>', methods=["GET", "POST"])
# def questions_wrong(question_num, questions_score, passed_on, lives, guess, username):
#   questions = get_questions()
#   q_num = int(question_num) - 1
#   question = questions[0][q_num]
#   answer = questions[1][q_num]
  
#   message = "'{0}', Was Incorrect".format(guess)
#   lives = str(int(lives) - 1)
#   bg = "#FF4D4C"
  
#   if request.method == "POST":
#     guess = request.form["answer"]
    
#     url = check_guess(answer, guess, lives, question_num, questions_score, passed_on, username)
    
#     return url
  
#   return render_template(
#     "questions.html",
#     message=message,
#     question=question,
#     lives=lives,
#     questionNum=question_num,
#     questionsScore=questions_score,
#     passed=passed_on,
#     bg=bg,
#     username=username
#     ) 
    
    
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