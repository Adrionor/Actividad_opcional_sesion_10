from .operations import get_fractions

def test_get_fractions():
    # Number as a string
    # "10" = 10
    result_fra1 = get_fractions(10)
    #print(f"Expected 1 ... got {result_fra1}")
    assert result_fra1 == 10

#test_get_fractions(10)

def test_get_fractions_2():
    # Numbers as a string and with / operator
    # "7/4" = 1.75
    result_fra2 = get_fractions(7/4)
    #print(f"Expected 1.75 ... got {result_fra2}")
    assert result_fra2 == 1.75

#test_get_fractions_2(7/4)

def test_get_fractions_3():
    # Negative number as a string
     # "-1") = -1
    result_fra3 = get_fractions(-1)
    #print(f"Expected -1 ... got {result_fra3}")
    assert result_fra3 == -1

#test_get_fractions_3(-1)