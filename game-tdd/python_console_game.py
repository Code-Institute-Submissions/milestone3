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
        else: return True
            
    
def add_username():
    username = input("Enter a Username\n>")
    
    if verify_username(username):
        file = open("users_test.txt", "a")
        file.write(username + "\n")
        file.close()
        
        print("\nWelcome " + username + "\n")
        return True
    

def game_loop():
    add_username()
    
        

game_loop()