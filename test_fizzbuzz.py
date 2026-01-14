# start of with a faliling test 

from main import fizzbuzz 

# def test_number():
#     assert fizzbuzz(1) == 1

def test_fizz():
    assert fizzbuzz(6) == "Fizz"

# now lets test buzz 

def test_buzz():
    assert fizzbuzz(10) == "Buzz"

# now test FizzBuzz

def test_fizzbuzz():
    assert fizzbuzz(30) == "FizzBuzz"