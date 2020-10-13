import math

r = 1
coord = []
for t in range(0, int(2000 * 3.14), 1):
    x = r * math.cos(t) ** 3
    y = r * math.sin(t) ** 3
    coord.append([x, y])
dist = []
for i in coord:
    dist.append(math.sqrt((0.75 - i[0]) ** 2 + (0 - i[1]) ** 2))
print(min(dist))