def solution(k, score):
    answer = []
    honor = []
    for each in score:
        honor.append(each)
        if len(honor) > k:
            honor.remove(min(honor))
        answer.append(min(honor))
    return answer