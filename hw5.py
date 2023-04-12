def read_single_digit(digit):
    if (digit == 0):
        return '영'
    elif (digit == 1):
        return '일'
    elif (digit == 2):
        return '이'
    elif (digit == 3):
        return '일'
    elif (digit == 4):
        return '사'
    elif (digit == 5):
        return '오'
    elif (digit == 6):
        return '육'
    elif (digit == 7):
        return '칠'
    elif (digit == 8):
        return '팔'
    elif (digit == 9):
        return '구'


def read_number():
    num = int(input("세 자리 정수 입력 : "))

    first = read_single_digit(num//100)
    second = read_single_digit((num % 100)//10)
    third = read_single_digit(num % 10)

    print(f'{first} {second} {third}')


read_number()
