import hashlib


def make_token(username, password):
    s = username + password
    # print(s)
    return hashlib.md5(s.encode()).hexdigest()


def save_token(username, password):
    with open('token.txt', 'w') as f:
        f.write(make_token(username, password))


def get_token():
    with open('token.txt') as f:
        info = f.read().strip()
        # print(info)
    return info


def login_required(func):
    def wrapper(*args, **kwargs):
        i = 3
        while i > 0:
            user = input()
            password = input()
            if get_token() == make_token(user, password):
                return func(*args, **kwargs)
            i -= 1
            return None
    return wrapper


# @login_required
# def f1():
#     print('Функция защищена паролем')
#
#
# @login_required
# def f2():
#     print('Эта функция тоже защищена паролем')
#
#
# f1()
# f2()
