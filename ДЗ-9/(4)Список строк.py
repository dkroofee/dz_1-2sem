lst = [x for x in input().split()]
print("[", sep="")
for i in range(len(lst)-1):
    print("'", lst[i], "'", ", ", sep="", end="")
print("'", lst[-1], "'", "]", sep="")