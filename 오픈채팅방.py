def solution(records):
    verb_queue = []
    id_queue = []
    nickname_map = {}
    verb_map = {'Enter' : '들어왔습니다.', 'Leave' : '나갔습니다.'}

    for record in records:
        record_array = record.split()
        if len(record_array) > 2:
            nickname_map[record_array[1]] = record_array[2]
    answer = []
    for record in records:
        record_array = record.split()
        user_verb = record_array[0]
        user_id = record_array[1]
        if user_verb in verb_map:
            user_statement = nickname_map[user_id] + '님이 ' + verb_map[user_verb]
            answer.append(user_statement)
    return answer