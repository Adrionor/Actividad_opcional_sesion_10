from .operations import multiply

def test_multiply():
    # Negative numbers
    # "-2" * "3" = -6
    # Insert your code here
    result_m1 = multiply(-2, 3)
    #print(f"Expected -6 ... got {result_m1}")
    assert result_m1 == -6

#test_multiply (-2,3)

def test_multiply_2():
    # Fractions
    # "1/2" * "8/4" = 1
    # Insert your code here
    result_m2 = multiply(1/2, 8/4)
    print(f"Expected 1 ... got {result_m2}")
    assert result_m2 == 1

#test_multiply_2("1/2","8/4")

def test_multiply_3():
    # Positive numbers
    # "10" * "5" = 50
    # Insert your code here
    result_m3 = c.multiply(10,5)
    print(f"Expected 50 ... got {result_m3}")
    assert result_m3 == 50

#test_multiply_3("10","5")
