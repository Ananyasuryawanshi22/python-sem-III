from datetime import datetime

def log(func):
    def display():
        print("Function Name:", func.__name__)
        print("Called At:", datetime.now())
        func()
    return display

def greet():
    print("Welcome!")

greet = log(greet)

greet()