a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = int(input('Введите номер месяца (от 1 до 12): ')) - 1
year = int(input('Введите год: '))
is_vis = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
if is_vis and month == 1:
    print(29)
else:
    print(a[month])