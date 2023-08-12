import operations as c

def test_multiply(num1,num2):
    # Negative numbers
    # "-2" * "3" = -6
    # Insert your code here
    result_m1 = c.multiply(num1, num2)
    print(f"Expected -6 ... got {result_m1}")

test_multiply (-2,3)

def test_multiply_2(num1,num2):
    # Fractions
    # "1/2" * "8/4" = 1
    # Insert your code here
    result_m2 = c.multiply(num1, num2)
    print(f"Expected 1 ... got {result_m2}")

test_multiply_2("1/2","8/4")

def test_multiply_3(num1,num2):
    # Positive numbers
    # "10" * "5" = 50
    # Insert your code here
    result_m3 = c.multiply(num1, num2)
    print(f"Expected 50 ... got {result_m3}")

test_multiply_3("10","5")
