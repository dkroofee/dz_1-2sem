n = input()
check = int(n[0])
while (int(n) < 10**9) and (check != 1):
    n = check * int(n)
    check = int(str(n)[0])
    print(n, check)
print(n)