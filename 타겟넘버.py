from collections import deque

def solution(numbers, target):
    array_len = len(numbers)
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    
    while queue:
        num_sum, num_idx = queue.popleft()
        if num_idx == array_len - 1:
            if num_sum == target:
                answer += 1
        else:
            queue.append([num_sum + numbers[num_idx + 1], num_idx + 1])
            queue.append([num_sum - numbers[num_idx + 1], num_idx + 1])
            
    return answer;