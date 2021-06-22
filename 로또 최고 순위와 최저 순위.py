def solution(lottos, win_nums):
    
    count_zero = lottos.count(0)
    count_match = 0
    for num in lottos:
        if num in win_nums:
            count_match += 1
    return [calculate_winner(count_match + count_zero), calculate_winner(count_match)]

def calculate_winner(num):
    wins = [6, 6, 5, 4, 3, 2, 1]
    return wins[num]