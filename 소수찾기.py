from itertools import permutations
import math

def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        per_list = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(per_list)):
            if check(int(i)):
                answer.append(int(i))
    answer = len(set(answer))

    return answer

def check(n):
    k = math.sqrt(n)
    if n < 2: 
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True