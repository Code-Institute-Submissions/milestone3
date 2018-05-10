# Check wether username given is blank, already taken or valid
def verify_username(username):
    if username == "":
        print("Username Cannot Be Left Blank!\n")
        return False
    
    with open("users_test.txt", "r") as file:
        users = file.read().splitlines()
        
    for user in users:
        if user == username:
            print("Username already used, please choose another\n")
            return False
    return True

#Takes username as an input value, if valid it adds it to users_test.txt file
def add_username():
    username = input("Enter a Username\n>")
    
    if verify_username(username):
        file = open("users_test.txt", "a")
        file.write(username + "\n")
        file.close()
        
        print("\nWelcome " + username + "\n")
        return True
    else: add_username()


# This function will take questions from questions_test.txt and loop through them.
def questions():
    print("It's question time!\n")
    questions = []
    answers = []
    
    with open("questions_test.txt", "r") as file:
        lines = file.read().splitlines()
        
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
            
    questions_and_answers = zip(questions, answers)
    question_num = 0
            
    for question, answer in questions_and_answers:
        question_num += 1
        guess = input("Question {0} > {1}\n".format(question_num, question))
        
        if guess == answer:
            print("Correct")
        else:
            print("Wrong!")
            
    

# Game functionality
def game_loop():
    add_username()
    questions()
        

game_loop()