def is_head(a, b):
    for i in range(len(a)):
        if not a[i] == b[i]:
            return False
    return True

def solution(phone_book):
    length = len(phone_book)
    phone_book.sort()
    print(phone_book)
    for i in range(length-1):
        a = phone_book[i]
        b = phone_book[i+1]
        if len(a)<len(b) and is_head(a, b):
            return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))