from operations import substract

def test_substract(num1, num2):
    # Float numbers
    # "0.5" - "0.5" = 0
    result_sub1 = substract(num1, num2)
    print(f"Expected 0 ... got {result_sub1}")

test_substract("0.5","0.5")
    


def test_substract_2(num1, num2):
    # Fraction numbers
    # "1/2" - "1" = -0.5
    # Insert your code here
    result_sub2 = substract(num1, num2)
    print(f"Expected -0.5 ... got {result_sub2}")
test_substract_2("1/2","1")


def test_substract_3(num1, num2):
    # Result negative
    # "10" - "5" = 5
    result_sub3 = substract(num1, num2)
    print(f"Expected 5 ... got {result_sub3}")
test_substract_3("10","5")
 

