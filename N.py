import math
def solution(arr):
    answer = 1
    for num in arr:
        gcd = math.gcd(answer, num)
        answer = int(answer * num / gcd)
    return answer