def counter(func):
    count = 0

    def display():
        nonlocal count
        count += 1
        print("Function called", count, "times")
        func()

    return display

def greet():
    print("Hello!")

greet = counter(greet)

greet()
greet()
greet()