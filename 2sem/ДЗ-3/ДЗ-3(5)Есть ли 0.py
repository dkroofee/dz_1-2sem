i = input().split()
lst = [i]
while i != '':
    i = input()
    lst.append(i.split())
print(any(int(x) == 0 for j in lst for x in j))