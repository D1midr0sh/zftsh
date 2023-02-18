a = list(map(int, input('Введите массив в одну строку: ').split()))
m = a[0]
for i in a:
    if i > m:
        m = i
print(m)