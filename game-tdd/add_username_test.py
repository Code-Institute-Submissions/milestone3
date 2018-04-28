usernames = ["myName", "skycat92"]

def add_username(username):
    if username == "":
            return False
    
    for user in usernames:
        if username == user:
            print(user + " already exists")
            return False
            
    usernames.append(username)
    print("username is unique!")
    print(usernames)
    return True




assert add_username("") == False, "No username given"
assert add_username("skycat92") == False, "Username already exists"
assert add_username("bob123") == True, "Username added"



# Checks to see if username exists in usernames[]
def test_is_in_collection(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
test_is_in_collection(usernames, "bob123")


print("All Tests Pass!")