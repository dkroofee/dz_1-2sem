n = int(input())
for i in range(2, n):
    for j in range(2, i + 1):
        if i % j != 0 or j == i:
            if j == i:
                print(i)
            else:
                continue
        elif i % j == 0:
            break
