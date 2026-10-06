n = int(input("Введите количество чисел: "))
sum_positive = 0
count_positive = 0

sum_negative = 0
count_negative = 0

for i in range(N):
  x = int(input("Введите число: "))
  if x > 0:
    sum_positive += x
    count_positive += 1
  elif x < 0:
    sum_positive += x
    count_positive += 1

if count_positive > 0 and count_negtive > 0:
  average_positive = sum_positive / count_positive
  average_negative = sum_negative / count_negative

  result = average_positive * average_negative
  print("Произведение =", result)
else:
  print("Нет положительных или отрицательных чисел")
    
