from .operations import substract

def test_substract():
    # Float numbers
    # "0.5" - "0.5" = 0
    result_sub1 = substract(0.5,0.5)
    print(f"Expected 0 ... got {result_sub1}")
    assert result_sub1 == 0

#test_substract("0.5","0.5")
    


def test_substract_2():
    # Fraction numbers
    # "1/2" - "1" = -0.5
    # Insert your code here
    result_sub2 = substract(1/2, 1)
    print(f"Expected -0.5 ... got {result_sub2}")
    assert result_sub2 == -0.5
#test_substract_2("1/2","1")


def test_substract_3():
    # Result negative
    # "10" - "5" = 5
    result_sub3 = substract(10,5)
    print(f"Expected 5 ... got {result_sub3}")
    assert result_sub3 == 5
#test_substract_3("10","5")
 

