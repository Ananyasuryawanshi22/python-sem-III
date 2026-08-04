def validate(func):
    def check(*args):
        for i in args:
            if type(i) != int:
                print("Error: All arguments must be positive integers.")
                return
        func(*args)
    return check

def add(a, b):
    print("Sum =", a + b)

add = validate(add)

add(10, 20)     
add(10, -5)     