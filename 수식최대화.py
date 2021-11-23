from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    pool = ['+', '-', '*']
    expression_list = []
    start = 0
    for i, char in enumerate(expression):
        if char in pool:
            expression_list.append(expression[start:i])
            expression_list.append(char)
            start = i + 1
    expression_list.append(expression[start:])

    primarity = permutations(당구)
    for case in primarity:
        stacks = [deque(expression_list), deque()]
        t1 = 1
        for c in case:
            t1 = (t1+1) % 2
            t2 = (t1+1) % 2
            while len(stacks[t1]):
                item = stacks[t1].popleft()
                if len(stacks[t2]) and stacks[t2][-1] == c:
                    c = stacks[t2].pop()
                    n = stacks[t2].pop()
                    item = str(eval(str(n) + c +str(item)))
                stacks[t2].append(item)

        result = stacks[len(당구) % 2].pop()
        result = abs(int(result))
        answer = max(answer, result)
    return answer