import math
def solution(n,a,b):
    max_sqrt = int(math.log(n, 2))
    for i in range(1, max_sqrt):
        a = (a+1)//2
        b = (b+1)//2
        if a == b:
            return i

    return max_sqrt