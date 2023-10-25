# Functions are blocks of code that you can call repeatedly

def do_something():
    print("DO SOMETHING PLEASE")

do_something()
do_something()

###

# Functions can also take in parameters, which are then used as variables inside the function

def do_something_with_number(number):
    print("DO SOMETHING WITH THIS PLEASE: ", number)

do_something_with_number(1)
do_something_with_number(5)

###

# Functions may also return values computed within it

def is_number_less_than_5(number):
    check = number < 5
    return check

if is_number_less_than_5(10):
    print("Number is less than 5")
else:
    print("Number is NOT less than 5")