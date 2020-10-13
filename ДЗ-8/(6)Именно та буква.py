st, fav_num, fav_letter = input(), int(input()), input()
if st[fav_num-1] == fav_letter:
    print("YES")
elif len(fav_letter) != 1:
    print("MISTAKE")
else:
    print("NO")