def solution(n, t, m, timetable):

    def mn_st(mn):
        h = str(mn//60)
        m = str(mn%60)
        if len(h)==1:
            h = '0'+h
        if len(m)==1:
            m = '0'+m
        return h+':'+m

    def st_mn(st):
        h, m = map(int, st.split(':'))
        return h*60 + m

    buses = [m]*n
    bus_times = [mn_st(540 + i*t) for i in range(n)]
    timetable.sort()
    last_crew = 0

    for c_i in range(len(timetable)):
        crew = timetable[c_i]
        for i in range(n):
            if buses[i] and bus_times[i]>=crew:
                buses[i]-=1
                last_crew = c_i
                break
    last_crew = mn_st(st_mn(timetable[last_crew]) - 1)

    if buses[-1]:
        return bus_times[-1]
    return last_crew




print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))