from python_pytest.fizzbuzz import fizzbuzz

#fizz_buzz(3) ➞ "Fizz"
def test_fizz():
    # given
    num = 3

    # when
    result = fizzbuzz(num)

    # then
    assert result == "Fizz"

#fizz_buzz(5) ➞ "Buzz"
def test_buzz():
    # given
    num = 5

    # when
    result = fizzbuzz(num)

    # then
    assert result == "Buzz"

#fizz_buzz(15) ➞ "FizzBuzz"
def test_fizzbuzz():
    # given
    num = 15

    # when
    result = fizzbuzz(num)

    # then
    assert result == "FizzBuzz"

#fizz_buzz(4) ➞ "4"
def test_fizzbuzz_string_number():
    # given
    num = 4

    # when
    result = fizzbuzz(num)

    # then
    assert result == "4"

#fizz_buzz("a") ➞ None
def test_fizzbuzz_none():
    # given
    num = "a"

    # when
    result = fizzbuzz(num)

    # then
    assert result == None

#fizz_buzz("") ➞ None
def test_fizzbuzz_empty():
    # given
    num = ""

    # when
    result = fizzbuzz(num)

    # then
    assert result == None