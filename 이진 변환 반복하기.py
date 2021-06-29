def solution(s):
    cnt_zero = 0
    cnt_after_zero = 0
    
    while s != '1':
        cnt_zero += s.count('0')
        s = [i for i in s if i != '0'] 
        length = len(s)
        s = bin(length)[2:] 
        cnt_after_zero += 1	

    return [cnt_after_zero, cnt_zero]