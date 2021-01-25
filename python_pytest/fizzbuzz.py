def fizzbuzz(number):
    '''Takes a number and returns "Fizz", "Buzz" of "FizzBuzz"'''
    if number == "" or isinstance(number, str):
        return None
    #If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    #If the number is a multiple of 3 the output should be "Fizz".
    elif number % 3 == 0:
        return "Fizz"
    #If the number given is a multiple of 5, the output should be "Buzz".
    elif number % 5 == 0:
        return "Buzz"
    #If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
    else:
        return str(number)