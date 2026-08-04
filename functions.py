def add(a, b):
    print("Required Arguments:")
    print("Sum =", a + b)

def student(name, age):
    print("\nKeyword Arguments:")
    print("Name:", name)
    print("Age:", age)

def greet(name, message="Welcome!"):
    print("\nDefault Arguments:")
    print(message, name)

def total(*numbers):
    print("\nVariable-Length Arguments:")
    print("Numbers:", numbers)
    print("Sum =", sum(numbers))


add(10, 20)                        

student(age=20, name="Rahul")      

greet("Anita")                     
greet("Anita", "Good Morning!")    

total(10, 20, 30)                  
total(5, 10, 15, 20, 25)