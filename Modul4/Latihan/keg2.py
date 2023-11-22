import os

def uppercase_decorator(function):
    def wrapper():
        func_result = function()
        make_uppercase = func_result.upper()
        return make_uppercase
    return wrapper

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

@uppercase_decorator
def say_hi():
    return 'hello there'

result = say_hi()
print(result)