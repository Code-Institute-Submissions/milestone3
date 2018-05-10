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
    
    
    # Simple manual test to make sure questions and answers are going to correct list
    print("Questions >\n")
    print(questions)
    print("\n")
    print("Answers > \n")
    print(answers)
            

questions()