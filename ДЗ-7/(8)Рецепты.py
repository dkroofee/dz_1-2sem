M = int(input())
products = set()
rec = set()
for i in range(M):
    products.add(input())
N = int(input())
for i in range(N):
    recipe = input()
    ing = int(input())
    for j in range(ing):
        food = set()
        food.add(input())
    n = products >= food
    if n == True:
        rec.add(recipe)
print(*rec, sep='\n')
