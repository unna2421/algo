from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    candidates = []
    for i in range(1, col+1):
        candidates.extend(combinations(range(col), i))

    unique = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if(len(set(tmp))) == row:
            unique.append(keys)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i])==len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])
    return len(answer)