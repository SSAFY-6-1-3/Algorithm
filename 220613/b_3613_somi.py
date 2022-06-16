def java_to_c():
    ans = []
    for i in range(len(name_ord)):
        if 65 <= name_ord[i] <= 90:  # 대문자
            ans.append('_' + chr(name_ord[i] + 32))  # 대문자 => 밑줄 + 소문자
        elif 97 <= name_ord[i] <= 122:  # 소문자
            ans.append(name_list[i])
        else:
            return 'Error!'
    return ans


def c_to_java():
    ans = []
    i = 0
    while i < len(name_ord):
        if name_ord[i] == 95:
            if 97 <= name_ord[i + 1] <= 122:
                ans.append(chr(name_ord[i + 1] - 32))  # 밑줄 + 소문자 => 대문자
                i += 2
            else:
                return 'Error!'  # 밑줄 다음에 소문자 아니면 에러
        elif 97 <= name_ord[i] <= 122:  # 소문자
            ans.append(name_list[i])
            i += 1
        else:  # 밑줄, 소문자 이외의 문자는 에러
            return 'Error!'
    return ans


name = input()
name_list = list(name)
name_ord = list(map(lambda x: ord(x), name))
small_chr = list(filter(lambda x: 97 < x < 122, name_ord))

if len(small_chr) == len(name_list):  # 전부 소문자면 안바꿔도 됨
    print(name)

elif 95 in name_ord:  # 밑줄이 있다면 C++
    if name_ord[0] == 95 or name_ord[-1] == 95:  # 맨 처음이나 맨 끝에 있으면 안됨
        print('Error!')
    else:
        tmp = c_to_java()
        print(''.join(tmp))

else:
    if 65 <= name_ord[0] <= 90:  # 처음부터 대문자는 에러
        print('Error!')
    else:
        tmp = java_to_c()
        print(''.join(tmp))



# print(ord('A')) # 65
# print(ord('Z')) # 90
# print(ord('a')) # 97
# print(ord('z')) # 122

# print(chr(122-32)) # Z
# print(ord('_')) # 95

