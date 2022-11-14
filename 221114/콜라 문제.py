def solution(a, b, n):
    answer = 0
    while True:
        if n < a:
            break
        submit_bottle = n // a * a
        return_bottle = n // a * b
        extra_bottle = n - submit_bottle
        n = extra_bottle + return_bottle
        answer += return_bottle
    return answer