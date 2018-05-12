# This function will take three arguments: correct answers (C), questions passed on (P), and lives left (L)
def final_score(C, P, L):
    answers_score = C * 50
    lives_score = L * 25
    
    # I have used integer division // to get an integer result, discarding any fractional result
    passed_score = (P//3)*40
    
    final_score = answers_score + lives_score - passed_score
    
    return final_score


# TESTS
def test_if_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

test_if_equal(final_score(0,0,0),0)
test_if_equal(final_score(15,0,0),750)
test_if_equal(final_score(15,0,2),800)
test_if_equal(final_score(18,3,2),910)
test_if_equal(final_score(9,11,1),355)


print("All Tests Pass!")