def fibonacci(number):
    i = 0
    j = 1
    while i < number:
        yield i
        i, j = j, i + j

# for n in fibonacci(10):
#     print (n)


