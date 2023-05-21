N = int(input('Введите трехзначное число: '))

while N < 100 or N > 999:
    print('Вы ввели не трехзначное число')
    N = int(input('Введите трехзначное число: '))

digit1 = N // 100
digit2 = (N // 10) % 10
digit3 = N % 10

print(f'Сумма цифр трехзначного числа: {digit1 + digit2 + digit3}')