from .operations import sum

def test_sum():
    # Floats
    # "0.5" + "0.5" = 1
    result_sum1 = sum(0.5,0.5)
    #print(f"Expected 1 ... got {result_sum1}")
    assert result_sum1 == 1

#test_sum("0.5","0.5")

def test_sum_2():
    # Negative numbers
    # "-3" + "-3" = -6
    result_sum2 = sum(-3,-3)
    #print(f"Expected -6 ... got {result_sum2}")
    assert result_sum2 == -6

#test_sum_2("-3","-3")

def test_sum_3():
    # Positive numbers
    # "4" + "6" = 10
    # Insert your code here
    result_sum3 = sum(4,6)
    #print(f"Expected 10 ... got {result_sum3}") 
    assert result_sum3 == 10

#test_sum_3(4,6)