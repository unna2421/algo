def solution(n):
    answer = 0
    result = ''
    while n >= 1:
        rest = n % 3
        n //= 3
        result += str(rest)
    return int(result,3)