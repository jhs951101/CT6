print('1~100까지에서 3과 8의 공배수 : ', end='')
n = 1

while n <= 100:
    if n%3 == 0 and n%8 == 0:
        print(str(n) + '   ', end='')

    n += 1
