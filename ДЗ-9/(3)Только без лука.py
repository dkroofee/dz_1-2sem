n, recipe = int(input()), []
for i in range(n):
    product_or_action = input().lower()
    if "лук" not in product_or_action:
        recipe.append(product_or_action)
print(*recipe)