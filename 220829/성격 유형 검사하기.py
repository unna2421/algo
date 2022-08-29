from collections import defaultdict

def solution(survey, choices):
    answer = ''
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    survey_dict = defaultdict(int)
    
    for i in range(len(survey)):
        survey_dict[survey[i][choices[i] // 4]] += score[choices[i]]
        
    answer += 'R' if survey_dict['R'] >= survey_dict['T'] else 'T'
    answer += 'C' if survey_dict['C'] >= survey_dict['F'] else 'F'
    answer += 'J' if survey_dict['J'] >= survey_dict['M'] else 'M'
    answer += 'A' if survey_dict['A'] >= survey_dict['N'] else 'N'
        
    return answer