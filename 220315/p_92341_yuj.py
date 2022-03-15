import math

def solution(fees, records):
    lst = []
    results = {}
    for record in records:
        time, car, state = map(str, record.split())
        if car in results:
            results[car].append(time)
        else:
            results[car] = [time]

    for result in results:
        total = 0

        if len(results[result]) % 2:
            results[result].append('23:59')

        for i in range(len(results[result]) // 2):
            start = results[result][2 * i]
            end = results[result][2 * i + 1]

            if int(end[3:5]) >= int(start[3:5]):
                total += (int(end[0:2]) - int(start[0:2])) * 60
                total += int(end[3:5]) - int(start[3:5])
            else:
                total += (int(end[0:2]) - int(start[0:2]) - 1) * 60
                if int(end[3:5]) == 0:
                    total += 60 - int(start[3:5])
                else:
                    total += 60 + int(end[3:5]) - int(start[3:5])
        lst.append([result, total])

    lst.sort()
    answer = []

    for money in lst:
        fee = 0
        if money[1] >= fees[0]:
            fee += fees[1]
            fee += (math.ceil((money[1] - fees[0]) / fees[2]) * fees[3])
        else:
            fee += fees[1]
        answer.append(fee)
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))

