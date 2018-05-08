# Tests will be carried out to determine if a username is unique after reading users.txt file

def verify_username(username):
    if username == "":
        return False
    
    with open("users_test.txt", "r") as file:
        users = file.read().splitlines()
        
    for user in users:
        if user == username:
            return False
            
    file = open("users_test.txt", "a")
    file.write(username + "\n")
    file.close()
    return True
        



assert verify_username("") == False, "username was left blank"
assert verify_username("bob123") == True, "Username was added to users.txt"
assert verify_username("skycat92") == False, "Username already existss"

print("All Tests Pass")