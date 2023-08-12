import operations as c

def test_divide(num1, num2):
    # Fraction
    # 10/2 = 5
    result1 = c.divide(num1, num2)
    print(f"Expected 5 ... got {result1}")

test_divide(10, 2)

def test_divide_2(num1,num2):
    # Strings and divisions
    # "-15/4" / "1/2" =  -7.5 
    result2 = c.divide(num1, num2)
    print(f"Expected -7.5 ... got {result2}")

test_divide_2("-15/4", "1/2")

def test_divide_3(num1,num2):
    # Strings and divisions
    # "8"/"16" = 0.5
    result3 = c.divide(num1, num2)
    print(f"Expected 0.5 ... got {result3}")

test_divide_3("8", "16")
