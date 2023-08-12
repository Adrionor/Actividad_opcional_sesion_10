from operations import sum

def test_sum(num1, num2):
    # Floats
    # "0.5" + "0.5" = 1
    result_sum1 = sum(num1, num2)
    print(f"Expected 1 ... got {result_sum1}")

test_sum("0.5","0.5")

def test_sum_2(num1, num2):
    # Negative numbers
    # "-3" + "-3" = -6
    result_sum2 = sum(num1, num2)
    print(f"Expected -6 ... got {result_sum2}")

test_sum_2("-3","-3")

def test_sum_3(num1, num2):
    # Positive numbers
    # "4" + "6" = 10
    # Insert your code here
    result_sum3 = sum(num1, num2)
    print(f"Expected 10 ... got {result_sum3}") 

test_sum_3(4,6)