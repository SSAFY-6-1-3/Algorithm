N = int(input())

books = {}  # {'title' : 횟수}
for _ in range(N):
    book = input()
    if books.get(book):  # 만약 이미 딕셔너리에 저장된 책 제목이라면
        books[book] += 1 # value 값 1 증가
    else:                # 아직 딕셔너리에 추가 안된 책이라면
        books[book] = 1  # key, value 딕셔너리에 추가

book_list = sorted(list([title, count] for title, count in books.items()), key= lambda x: x[1], reverse=True) # 책 판매 순으로 sort 한 리스트 생성
title = [book_list[0][0]] # 일단 가장 첫 책을 먼저 저장

for i in range(1, len(book_list)):
    if book_list[i][1] == book_list[0][1]:  # 만약 같은 판매량이 있는 경우
        title.append(book_list[i][0])       # 책 제목을 append
    else:
        break


title.sort()     # 책 제목순으로 sort
print(title[0])  # 가장 첫 책 제목 print

