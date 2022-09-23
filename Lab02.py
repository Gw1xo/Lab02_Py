import math
# Task 1
print("\nTask 1")
rez = []
for i in range(3):
    num = int(input("Введіть ціле число:"))
    if (num <= 3) and (num >= 1):
        rez.append(num)
print(f"Результат: {rez}")

# Task 2
print("\nTask 2")
year = int(input("Введіть рік: "))
while True:
    # застосовуємо guard clause
    if (year % 100 == 0) and (year % 400 != 0):
        print("Кількість днів у році: 365 ")
        break
    if year % 4 == 0:
        print("Кількість днів у році: 366 ")
        break
    print("Кількість днів у році: 365 ")
    break

# Task 3
print("\nTask 3")
price = float(input("Введіть ціну:"))
discount = 0
if price >= 1000:
    discount = 6
elif price >= 500:
    discount = 3
print(f"До сплати:{price * ((100 - discount)/100) }")

# Task 4
print("\nTask 4")
initlist = []
for i in range(4):
    initlist.append(float(input("Введіть число:")))
initlist.sort()
print(f"Косинус мінімального: {math.cos(initlist[0])}")

# Task 5
print("\nTask 5")
initlist = []
for i in range(3):
    initlist.append(float(input("Введіть число:")))
initlist.sort()
print(f"Синус максимального: {math.sin(initlist[-1])}")

# Task 6
print("\nTask 6")
h = float(input("Введіть висоту трикутника:"))
b = float(input("Введіть довжину основи трикутника:"))
area = (b*h)/2
if area % 2 == 0:
    print(f"Площа поділена на 2:{area/2}")
else:
    print("Не можу ділити на 2!")

# Task 7
print("\nTask 7")
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
num = int(input("Введіть номер місяця:"))
print(f"Місяць англійською: {month[num-1]}")

# Task 8
print("\nTask 8")
nums = []
for i in range(3):
    nums.append(int(input("Введіть число:")))
print(f"Кількість позитивних: {len([i for i in nums if i>0])}")

# Task 9
print("\nTask 9")
A = int(input("Введіть А:"))
B = int(input("Введіть D:"))
print(f"Сума чисел між {A} i {B}: {sum([i for i in range(A, B+1)])}")

# Task 10
print("\nTask 10")
A = int(input("Введіть А:"))
B = int(input("Введіть D:"))
print(f"Сума квадратів чисел між {A} i {B}: {sum([i*i for i in range(A, B+1)])}")

# Task 11
print("\nTask 11")
a = int(input("Введіть a:"))
print(f"Середнє арифметичне чисел між {a} i 200: {sum([i for i in range(a, 201)])/200}")

# Task 12
print("\nTask 12")
A = int(input("Введіть А:"))
B = int(input("Введіть B:"))
suma = 0
while A <= B:
    suma += int(A)
    A += 1
print(f"Сума чисел між A i B: {suma}")

# Task 13
print("\nTask 13")
a = int(input("Введіть a:"))
print(f"Сума квадратів чисел між {a} i 50: {sum([i*i for i in range(a,51)])}")

# Task 14
print("\nTask 14")
N = int(input("Введіть N:"))
K = 0
while 5 ** K < N:
    K += 1
print(f"Найменше K при якій виконується умова 5 ** K > N : {K}")

# Task 15
print("\nTask 15")
n = int(input("Введіть n:"))
for i in list(map(lambda x: x**2, range(n))):
    if i > n:
        print(f"перше число, більше n: {i}")
        break

# Task 16
print("\nTask 16")
n = int(input("Введіть n:"))
num = 1
count = 0
step = list(i for i in range(n) if i % 2 != 0)
while n > num:
    num += step[count]
    count += 1
print(f"перше число, більше n: {num}")


