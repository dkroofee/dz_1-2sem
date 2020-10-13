M, N, K = int(input()), int(input()), int(input())
lst, lst_1 = [], []
for i in range(M + N + K):
    surname = input()
    if surname in lst:
        check = 0
        if surname in lst_1:
            lst_1.remove(surname)
            check = 1
        if check == 0:
            lst_1.append(surname)
            check = 0
    lst.append(surname)
if len(lst_1) == 0:
    print("NO")
else:
    print(len(lst_1))