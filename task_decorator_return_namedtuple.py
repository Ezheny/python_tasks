from collections import namedtuple


def return_namedtuple(*name):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            if isinstance(result, tuple):
                n_tuple = namedtuple('n_tuple', name)
                result = n_tuple(*result)
            return result
        return wrapper
    return decorator


# @return_namedtuple('one', 'two')
# def func():
#     return 1, 2
#
# r = func()
# print(r.one)
# print(r.two)
