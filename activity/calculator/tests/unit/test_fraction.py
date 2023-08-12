from operations import get_fractions

def test_get_fractions(num1):
    # Number as a string
    # "10" = 10
    result_fra1 = get_fractions(num1)
    print(f"Expected 1 ... got {result_fra1}")

test_get_fractions(10)

def test_get_fractions_2(num1):
    # Numbers as a string and with / operator
    # "7/4" = 1.75
    result_fra2 = get_fractions(num1)
    print(f"Expected 1.75 ... got {result_fra2}")

test_get_fractions_2(7/4)

def test_get_fractions_3(num1):
    # Negative number as a string
     # "-1") = -1
    result_fra3 = get_fractions(num1)
    print(f"Expected -1 ... got {result_fra3}")

test_get_fractions_3(-1)