n = int(input("Введите количество долек по горизонтали (n): "))
m = int(input("Введите количество долек по вертикали (m): "))
k = int(input("Введите количество долек, которое требуется отломить (k): "))

if k == n * m or k % n == 0 or k % m == 0:
    print("YES")
else:
    print("NO")