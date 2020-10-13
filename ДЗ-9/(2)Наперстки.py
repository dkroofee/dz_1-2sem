sod = list()
for i in range(int(input())):
    sod.append(input())
sod_per = list()
for j in range(int(input())):
    sod_per.clear()
    for i in range(int(input())):
        sod_per.append(sod[int(input()) - 1])
    sod.clear()
    sod = list(sod_per)
print(*sod, sep='\n')