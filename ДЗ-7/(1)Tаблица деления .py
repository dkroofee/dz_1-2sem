columns, strings = int(input()), int(input())

for i in range(1, strings+1):
    for j in range(1, columns+1):
        print((j/i), end=" ")
    print()
