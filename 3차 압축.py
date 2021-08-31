def solution(msg):
    dictionary = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    answer = []
    
    while len(msg) > 0:
        letter = msg[0]
        cnt = 0
        if len(msg) == 1:
            answer.append(dictionary.index(letter)+1)
            break
        while len(letter) < len(msg):
            s = letter
            cnt += 1
            letter += msg[cnt]
            if letter not in dictionary:
                letter = s
                break
        answer.append(dictionary.index(letter)+1)
        msg = msg[len(letter):]
        if msg:
            dictionary.append(letter + msg[0])
    return answer