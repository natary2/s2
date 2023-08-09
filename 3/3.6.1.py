
n = int(input("Количество цифр "))
sum = 0
for i in range(1, n + 1):
    x = int(input("Цифра "))
    if x == 0:
        sum += 1
print(sum)
