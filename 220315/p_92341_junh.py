import math

def time_check(i, o):
    it = int(i[:2])*60 + int(i[3:])
    ot = int(o[:2])*60 + int(o[3:])
    return ot-it

def calc(mnt, fees):
    kt, ky, ds, dy = fees
    if mnt <= kt:
        return ky
    cht = mnt-kt
    chy = math.ceil(cht/ds) * dy
    return ky + chy

def solution(fees, records):
    dict = {}
    t_dict = {}

    for rec in records:
        time, num, io = rec.split(' ')
        if io == "IN":
            dict[num] = time
        else:
            mnt = time_check(dict[num], time)
            dict.pop(num)
            if num in t_dict:
                t_dict[num] += mnt
            else:
                t_dict[num] = mnt

    for num, i in dict.items():
        mnt = time_check(i, "23:59")
        if num in t_dict:
            t_dict[num] += mnt
        else:
            t_dict[num] = mnt

    answer = []
    for n, m in sorted(t_dict.items()):
        answer.append(calc(m, fees))
    return answer



print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))