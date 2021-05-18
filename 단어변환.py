from collections import deque

def solution(begin, target, words):
    answer = 0
    visit = []
    queue = deque()
    queue.append([begin, 0])
    while queue:
        now, repeat = queue.popleft()
        if now == target:
            return repeat
        for word in can_change(now, words):
            if word not in visit:
                queue.append([word, repeat + 1])
                visit.append(word)
    return 0

def can_change(cur_word, words):
    can_word = []
    for word in words:
        diff = [True for x, y in zip(cur_word, word) if x != y]
        if len(diff) == 1: 
            can_word.append(word)
    return can_word