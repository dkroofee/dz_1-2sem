n, m = int(input()), int(input())
lib = [input() for i in range(n)]
summer_task = [input() for j in range(m)]
for k in range(len(summer_task)):
    if summer_task[k] in lib:
        print("YES")
    else:
        print("NO")