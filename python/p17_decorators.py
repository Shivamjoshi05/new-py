#Decorators is function that takes a function , it create a new function inside its body (wrapper).Then it returns that new function
def decorator(func):
    def wrapper():
        print("I am about to execute a fuction....")
        func()
        print("I have executed this function....")
    return wrapper

@decorator
def hello():
    print("Hello")

hello()

# f = decorator(hello)
# f()

