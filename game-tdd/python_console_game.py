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
    
    # If the username is valid adds it to users_test.txt
    if verify_username(username):
        file = open("users_test.txt", "a")
        file.write(username + "\n")
        file.close()
        
        print("\nWelcome " + username + "\n")
        return True
    else: add_username()
    
    
# Show scores
def show_scores(w,x,y,z):
    print("Correct!\nYour Score Is > {0}\nQuestions Passed > {1}\nLives Left > {2}\n".format(x,y,z))
    


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
            print("Wrong!\n")
            print("Your Incorrect Answer: {0}\n".format(guess))
            guess = input("Question {0} > {1}\n".format(question_num, question))
            
        if( guess == "pass" ):
            passed_on +=1
        else:
            questions_score += 50
            show_scores("correct",questions_score,passed_on,lives)
            
                
            
            
    

# Game functionality
def game_loop():
    add_username()
    questions()
        

game_loop()