def decorator(fun):
    def wrapper(*args, **kwargs):
        print(*args, **kwargs)
        result = fun(*args, **kwargs)
        return 1
    return wrapper

@decorator
def sum_test(a, b):
    print("call sum_test")
    print(a+b)

sum_test(2,3)