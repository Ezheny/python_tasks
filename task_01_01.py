year = int(input())
if (year // 100 and year % 400) or (year % 4):
    print('no')
else:
    print('yes')