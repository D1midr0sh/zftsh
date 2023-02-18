from random import randint

a = [randint(0, 144) for i in range(12)]
a.sort()  # Могу ещё написать сортировку пузырьком
print(*a)