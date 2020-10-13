n, m, symb = int(input()), int(input()), input()

print(symb * m)
for i in range(n-2):
    print(symb, end="")
    print(" " * (m-2), end="")
    print(symb)

print(symb * m, end="")