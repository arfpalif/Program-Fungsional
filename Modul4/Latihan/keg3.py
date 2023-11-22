import os

def title_case_decorator(func):
    def wrapper():
        result = func()
        make_title = result.title()
        print(make_title + " — Data is converted to title case")
        return make_title
    return wrapper

def split_string_decorator(func):
    def wrapper():
        result = func()
        splitted_string = result.split()
        print(str(splitted_string) + " — Then Data is splitted")
        return splitted_string
    return wrapper

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

@split_string_decorator
@title_case_decorator
def say_hi():
    return 'hello there'

# Memanggil fungsi yang telah di-decorate
result = say_hi()
print(result)