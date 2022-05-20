def val_checker(def_func):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not def_func(arg):
                    raise ValueError("error")
            res = func(*args)
            return res
        return wrapper
    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 5


print(calc_cube(5))
