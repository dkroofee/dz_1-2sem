def find_farthest_orbit(list_of_orbits):
    a = []
    for i in list_of_orbits:
        if i[0] == i[1]:
            a.append(0)
        else:
            a.append(3.14 * i[0] * i[1])

    c = a.index(max(a))
    return list_of_orbits[c]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))