def repeat(n):
    def decorators(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorators

@repeat(7)
def hello(a):
    print(f"hello {a}")

hello("Shivam")