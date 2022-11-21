def solution(number, limit, power):
    weights = 0
    for knight in range(1, number + 1):
        weapon = 0
        for num in range(1, int(knight ** 0.5) + 1):
            if knight % num == 0:
                weapon += 1
                if num ** 2 != knight:
                    weapon += 1
            if weapon > limit:
                weapon = power
                break
        weights += weapon
    return weights