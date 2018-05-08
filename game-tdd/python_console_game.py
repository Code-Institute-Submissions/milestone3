def add_username():
    username = input("Enter a Username\n>")
    if username == "":
        print("Username Cannot Be Left Blank!\n")
    else:
        print("\nWelcome " + username + "\n")
        return True
    


def game_loop():
    while True:
        add_username()
        if add_username():
            print("yay!")
        else:
            print("nay!")
        

game_loop()