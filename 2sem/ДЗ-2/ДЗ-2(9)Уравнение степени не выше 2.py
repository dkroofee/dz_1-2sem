def solve(*coef):
    if len(coef) == 1:
        if coef[0] == 0:
            return ['Любое значение']
        else:
            return [None]
    elif len(coef) == 2:
        return [-(coef[1] / coef[0])]
    elif len(coef) == 3:
        D = coef[1] ** 2 - 4 * coef[0] * coef[2]
        if D == 0:
            return [(-coef[1]) / (2 * coef[0])]
        elif D < 0:
            return [None]
        elif D > 0:
            return [(-coef[1] + D ** (1/2)) / (2 * coef[0]), (-coef[1] - D ** (1/2)) / (2 * coef[0])]
    else:
        return [None]


print(sorted(solve(1, 2, 4)))