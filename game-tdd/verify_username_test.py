# Tests will be carried out to determine if a username is unique after reading users.txt file





assert verify_username("") == False, "username was left blank"
assert verify_username("bob123") == True, "Username was added to users.txt"
assert verify_username("skycat92") == False, "Username already existss"

