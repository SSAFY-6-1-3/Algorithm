s = "one4seveneight"
result=""
word=""

number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

for idx in s:
    # 숫자이면 result에 추가
    if idx.isdigit():
        result += idx
    # 알파벳이면 word에 추가 -> word가 number에 key로 있으면 해당 value값을 result에 추가
    else:
        word += idx
        if word in number:
            result += str(number.get(word))
            word = ""
# "" 출력 안 되고 숫자만 출력되도록
print(result)