n = str(input()).split()
m = 0
lst2 = list()
for i in range(int(n[0])):
    product = str(input())
    if int(product[0:7]) * int(product[8:12]) == int(product[13:]):
        m += int(product[0:7]) * int(product[8:12])
    else:
        m += int(product[0:7]) * int(product[8:12])
        lst2.append(i + 1)
print(int(n[1]) - m)
print(*lst2)