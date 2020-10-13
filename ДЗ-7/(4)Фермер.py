money = int(input())
skot = int(input())
for i in range(1, money // 20 + 1):
    n = money - i * 20
    for j in range(n // 10 + 1):
        b = n - j * 10
        c = b // 5
        if b % 5 == 0:
            if i + j + c == 100:
                print(i, j, c)