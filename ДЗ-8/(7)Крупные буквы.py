n = input()
a = [' *   ', '* *  ', '***  ', '* *  ', '* *  ']
b = ['**   ', '* *  ', '**   ', '* *  ', '**   ']
c = [' *   ', '* *  ', '*    ', '* *  ', ' *   ']
for i in range(5):
    for j in range(len(n)):
        if n[j] == "A":
            print(a[i], end='  ')
        elif n[j] == 'B':
            print(b[i], end='  ')
        elif n[j] == 'C':
            print(c[i], end='  ')
    print()