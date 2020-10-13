N = input().split(';')
for i in range(len(N)):
    a = N[i].split(',')
    elem = list()
    for j in range(len(a)):
        if int(a[j]) >= 1000000000:
            elem.append(a[j])
    print(','.join(elem))