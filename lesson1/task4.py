number = int(input('Введите целое положительное число: '))
max_digit = 0
original_number = number

while number > 0:
    current_digit = number % 10
    if current_digit > max_digit:
        max_digit = current_digit
    number = int(number / 10)
print(f'Самая большая цифра из числа {original_number} - {max_digit}')





