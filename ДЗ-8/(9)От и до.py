lst = list()
for i in range(int(input())):
    lst.append(int(input()))
p = int(input())
q = int(input())
print(sum(lst[p - 1:q]))