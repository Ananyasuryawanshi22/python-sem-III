def login_required(func):
    def check():
        if logged_in:
            func()
        else:
            print("Access Denied! Please log in first.")
    return check

@login_required
def protected_function():
    print("Welcome! You have accessed the protected function.")

logged_in = True     
protected_function()