from .operations import divide

def test_divide():
    # Fraction
    # 10/2 = 5
    result1 = divide(10,2)
    #print(f"Expected 5 ... got {result1}")
    assert result1 == 5

#test_divide(10, 2)

def test_divide_2():
    # Strings and divisions
    # "-15/4" / "1/2" =  -7.5 
    result2 = divide("-15/4", "1/2")
    #print(f"Expected -7.5 ... got {result2}")
    assert result2 == -7.5

#test_divide_2("-15/4", "1/2")

def test_divide_3():
    # Strings and divisions
    # "8"/"16" = 0.5
    result3 = divide("8", "16")
    #print(f"Expected 0.5 ... got {result3}")
    assert result3 == 0.5

#test_divide_3("8", "16")
