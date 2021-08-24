def solution(files):
    files_len = len(files)
    
    for idx in range(files_len):
        first = ''
        second = ''
        number_start = False
        
        for char in files[idx]:
            if ord('0') <= ord(char) <= ord('9'):
                number_start = True
                second += char
            elif not number_start:
                first += char
            elif number_start:
                break
                
        first = first.lower()
        second = int(second)
        files[idx] = (files[idx], first, second)
        
    files.sort(key=lambda file: (file[1], file[2]))
    answer = [file[0] for file in files]
    return answer
        