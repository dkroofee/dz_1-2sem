houses_2 = set()
houses_1 = set()
new = input()
while new != "":
    houses_1.add(new)
    new = input()
new = input()
while new != "":
    houses_2.add(new)
    new = input()
result = houses_1 & houses_2
if result is not None:
    print(result)
else:
    print("EMPTY")