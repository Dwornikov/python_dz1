ticket_number = int(input("Введите номер билета (6 цифр): "))

if 100000 <= ticket_number <= 999999:
    digit6 = ticket_number % 10
    digit5 = ticket_number // 10 % 10
    digit4 = ticket_number // 100 % 10
    digit3 = ticket_number // 1000 % 10
    digit2 = ticket_number // 10000 % 10
    digit1 = ticket_number // 100000 % 10

    if digit1 + digit2 + digit3 == digit4 + digit5 + digit6:
        print("Билет", ticket_number, "является счастливым!")
    else:
        print("Билет", ticket_number, "не является счастливым.")
else:
    print("Некорректный номер билета. Пожалуйста, введите шестизначный номер.")
