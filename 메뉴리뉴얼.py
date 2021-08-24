import itertools
def solution(orders, answer_num):
    answer = []
    course_map = {}
    count_map = {}
    for num in answer_num:
        max_num = 0
        for order in orders:
            sort_order = sorted(order)
            course_combi = itertools.combinations(sort_order, num)
            for course in course_combi:
                course_key = ''.join(course)
                
                if course_key in course_map:
                    course_map[course_key] = course_map[course_key] + 1
                    max_num = course_map[course_key] if course_map[course_key] > max_num else max_num
                else:
                    course_map[course_key] = 1
        count_map[num] = max_num
    
    for key in list(course_map.keys()):
        if count_map[len(key)] != course_map[key]:
            del course_map[key]
        else:
            answer.append(key)
    return sorted(answer)