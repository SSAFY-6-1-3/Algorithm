def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: (x, len(x)))                      # 숫자 크기와 길이 순서대로 정렬
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            break

    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))