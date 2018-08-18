def lives_left(x):
    passed_questions = x
    
    if( passed_questions == 0 ):
        lives = 5
        print( "You still have {0} lives left".format(lives))
        return lives
    
    lives = 5   
    for i in range(passed_questions):
        
        i += 1
        print(i%3)
        
        if( i%3 == 0 ):
            lives -=1
            
            print("You Have {0} Lives Left".format(lives))
    return lives



# TESTS
def test_if_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

test_if_equal(lives_left(0),5)
test_if_equal(lives_left(3),4)




print("All Tests Pass!")