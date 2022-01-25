roseta = {
   	'zero': '0',
   	'one': '1',
   	'two': '2',
   	'three': '3',
   	'four': '4',
   	'five': '5',
   	'six': '6',
   	'seven': '7',
   	'eight': '8',
   	'nine': '9'
}

def solution(s):
    answer = ''
    s = list(s)

    while s:
        c = s.pop(0)
        if '0' <= c <= '9':
            answer += c
            continue
        c_num = c # on
        while c_num not in roseta:
            c_num += s.pop(0)

        answer += roseta[c_num]

    return int(answer)

print(solution("one4seveneight"))