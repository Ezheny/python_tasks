from time import sleep

def pause(sec):
    def decorator(func):
        def wrapper(*args, **kwargs):
            sleep(sec)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# @pause(2)
# def func():
#     print('Функция выполняется с задержкой 2 секунды!')
#
# func()