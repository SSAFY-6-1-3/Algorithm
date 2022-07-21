# 1. 첫번째 문자가 대문자이거나 _인 경우
# _가 2개 이상 연속으로 들어간 경우
# 마지막 문자가 '_'인 경우
# 알파벳, _ 이외에 다른 문자가 있는 경우
# 대문자와 _가 섞여 있는 경우
word = str(input())

if word[0].isupper() or word[0] == '_' or '__' in word or word[-1] == '_':
    print('Error!')

elif word.islower():
    alphas = word.split('_')
    for idx in range(len(alphas)):
        if not alphas[idx].isalpha():
            print('Error!')
            break
        if idx > 0:
            alphas[idx] = alphas[idx].capitalize()
    else:
        print(''.join(alphas))

else:
    result = ''
    for idx in range(len(word)):
        if word[idx].isalpha():
            if word[idx].isupper():
                result += '_'
                result += word[idx].lower()
            else:
                result += word[idx]
        else:
            print('Error!')
            break
    else:
        print(result)

