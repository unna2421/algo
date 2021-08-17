def solution(s):
    answer = 0
    for i in range(0, len(s)):
        string = s[i:len(s)] + s[0:i]
        if isRight(string):
            answer += 1
    return answer

def isRight(string):
    s_list = [s for s in string]
    stack = []
    for s in s_list:
        if stack and isPair(s, stack[-1]):
            stack.pop()
        else:
            stack.append(s)
    return not stack

def isPair(s1, s2):
    if s1 == ')' and s2 == '(':
        return True
    elif s1 == ']' and s2 == '[':
        return True
    elif s1 == '}' and s2 == '{':
        return True
    return False