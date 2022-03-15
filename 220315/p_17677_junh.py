def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()

    def jcd(a, b):
        if not a and not b:
            return 1
        h = len(a.union(b))
        g = len(a.intersection(b))
        return g/h
    # 대 65-90 소 97-122

    def str_set(st):
        ret = set()
        for i in range(len(st)-1):
            a, b = st[i], st[i+1]

            if (65<=ord(a)<=90 or 97<=ord(a)<=122) and (65<=ord(b)<=90 or 97<=ord(b)<=122):
                c = a+b
                while c in ret:
                    c = c+'-'
                ret.add(c)

        return ret

    answer = jcd(str_set(str1), str_set(str2)) * 65536
    return int(answer)





print(solution('FRANCE','french'))
print(solution('handshake','shake hands'))
print(solution('aa1+aa2','AAAA12'))