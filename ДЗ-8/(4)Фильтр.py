for i in range(int(input())):
    st = input()
    if (st[:2]) == "%%" :
        print(st[2::])
    elif (st[:4]) == "####":
        continue
    else:
        print(st)
