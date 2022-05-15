from itertools import combinations_with_replacement

def solution(n, info):
    answer = [0 for _ in range(11)]
    win = False
    max_num = 0
    for res in list(combinations_with_replacement(range(0, 11), n)):
        now = [0 for _ in range(11)]
        for r in res:
            now[10 - r] += 1
        lion = 0
        peach = 0
        for i, (l, p) in enumerate(zip(now, info)):
            if l == p == 0:
                continue
            if p >= l:
                peach += (10 - i)
            elif l > p:
                lion += (10 - i)
        if lion > peach:
            win = True
            if (lion - peach) > max_num:
                max_num = lion - peach
                answer = now
    if not win:
        return [-1]
    return answer