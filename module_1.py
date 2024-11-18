
print(9 ** 0.5 * 5)

print(9.99 > 9.98 and 1000 != 1000.1)

expr_without_priority = 2 * 2 + 2
expr_with_priority = 2 * (2 + 2)
print(expr_without_priority)
print(expr_with_priority)
print(expr_without_priority == expr_with_priority)

number_str = '123.456'
number = float(number_str)
number_shifted = number * 10  # Сместить дробную часть
first_digit_after_decimal = int(number_shifted) % 10  # Получить первую цифру после точки
print(first_digit_after_decimal)
