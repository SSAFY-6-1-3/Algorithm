import math

def solution(fees, records):
    answer = []

    car_dict = {}
    for record in records:
        time, car, status = record.split()
        if status == "IN":  # In
            if car not in car_dict:
                car_dict[car] = [[time, '23:59']]  # 2중리스트로 저장
            else: car_dict[car].append([time, '23:59'])
        else:  # Out
            car_dict[car][-1][1] = time

    for car in sorted(car_dict.items()):  # 차량 번호 작은 순
        time = 0  # 주차 한 총 시간
        for info in car[1]:
            in_h, in_m = map(int, info[0].split(':'))
            out_h, out_m = map(int, info[1].split(':'))
            time += (out_h - in_h) * 60 + (out_m - in_m)

        base_time, base_rate, plus_time, plus_rate = map(int, fees)
        if time <= base_time:
            answer.append(base_rate)
            continue

        answer.append(math.ceil((time - base_time) / plus_time) * plus_rate + base_rate)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))