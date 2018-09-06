# Check wether username given is blank, already taken or valid
def verify_username(username):
    if username == "":
        print("Username Cannot Be Left Blank!\n")
        return False
        
    # open users_test.txt and check wether the username is already taken
    with open("users_test.txt", "r") as file:
        users = file.read().splitlines()
        
    for user in users:
        if user == username:
            print("Username already used, please choose another\n")
            return False
    return True

#Takes username as an input value
def add_username():
    username = input("Enter a Username\n>")
    
    # While username is not verified
    while verify_username(username) == False:
        username = input("Enter a Username\n>")

    file = open("users_test.txt", "a")
    file.write(username + "\n")
    file.close()
        
    print("\nWelcome " + username + "\n")
    return username
    
    
# Show scores
def show_scores(w,x,y,z):
        if( w == "correct" ):
            print("\nCorrect!\nYour Score Is > {0}\nQuestions Passed > {1}\nLives Left > {2}\n".format(x,y,z))
        elif( w == "passed" ):
            print("\nQuestion Passed!\nYour Score Is > {0}\nQuestions Passed > {1}\nLives Left > {2}\n".format(x,y,z))
        else:
            print("\nWrong!\nYour Score Is > {0}\nQuestions Passed > {1}\nLives Left > {2}\n".format(x,y,z))
            
# Passed On
def question_passed(x,y):
    lives = y
    if x%3 == 0:
        lives -=1
    return lives
            
            
# Game Over
def game_over(x,y,z):
    print("\nGAME OVER!\n")
    if z == 0:
        print("YOU RAN OUT OF LIVES!\n")
    print("FINAL SCORE > {0}\nQuestions Passed > {1}\nLives Left > {2}\n".format(x,y,z))
    
    
# Save Username and Final Score to final_scores_test.txt
def save_final_score(x,y):
    with open("final_scores_test.txt", "a") as file:
        file.write("{0}\n".format(x))
        file.write("{0}\n".format(y))
        
        
        
# Show All Final Scores and Users
def show_final_scores():
    print("\nSCORE BOARD:\n")
    users = []
    scores = []
    
    # reads final_scores_test.txt and splits even lines into users and odd lines into scores
    with open("final_scores_test.txt", "r") as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if i%2 == 0:
            users.append(text)
        else:
            scores.append(text)
        
    #The zip() function gives a user and score tuple 
    users_and_scores = zip(users, scores)
    
    for user, score in users_and_scores:
        print("{0}-{1}\n".format(user, score))
    


    


# This function will take questions from questions_test.txt and loop through them.
def questions():
    print("It's question time!\n")
    questions = []
    answers = []
    
    # reads questions_test.txt and splits even lines into questions and odd lines into answers
    with open("questions_test.txt", "r") as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    #The zip() function gives a question and answer tuple 
    questions_and_answers = zip(questions, answers)
    question_num = 0
    questions_score = 0
    passed_on = 0
    lives = 5
    
            
    for question, answer in questions_and_answers:
        question_num += 1
        guess = input("Question {0} > {1}\n".format(question_num, question))
    
        while guess != answer and guess != "pass":
            lives -= 1
            if( lives == 0 ):
                game_over(questions_score,passed_on,lives)
                return questions_score
            show_scores("wrong",questions_score,passed_on,lives)
            print("Your Incorrect Answer: {0}\n".format(guess))
            guess = input("Question {0} > {1}\n".format(question_num, question))
            
        if( guess == "pass" ):
            passed_on +=1
            lives = question_passed(passed_on,lives)
            if( lives == 0 ):
                game_over(questions_score,passed_on,lives)
                return questions_score
            show_scores("passed",questions_score,passed_on,lives)
            
        else:
            questions_score += 50
            show_scores("correct",questions_score,passed_on,lives)
            
    game_over(questions_score,passed_on,lives)
    return questions_score
            
    
            

# Game functionality
def game_loop():
    user = add_username()
    final_score = questions()
    save_final_score(user,final_score)
    show_final_scores()
    
        

game_loop()