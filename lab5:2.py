N = int(input("Введите количество чисел: "))
a = []
for i in range(N):
  x = int(input("Введите число: "))
  a.append(x)

count = 0
summa = 0
for i in range (1, N):
  if a[i] > a[i - 1]:
    count += 1
    summa += a[i] - a[i -1]

print("Количество превышений:", count)
print("Сумма првышений:", summa)
