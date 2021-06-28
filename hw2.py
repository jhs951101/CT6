password = 'lovelive'
n = 1

while True:
    value = input('비밀번호 : ')

    if value == password:
        print('로그인 되었습니다!')
        break
    else:
        if n >= 3:
            print('로그인 실패! 횟수 초과!')
            break
        else:
            print('비밀번호를 다시 입력하세요.')

    n += 1
