import sys
sys.stdin = open('input.txt')

N = int(input())
books = {}                              # 책 제목, 책 개수 딕셔너리로 정리
for _ in range(N):
    book = input()

    if book in books:                   # 딕셔너리에 이미 있는 책일 경우 해당 value 1 증가
        books[book] += 1
    else:                               # 딕셔너리에 없다면 새로 만들어주기
        books[book] = 1

bestsellers = sorted(books.items(), key=lambda x:x[1])   # 딕셔너리 value에 따라 오름차순으로 정렬

bestseller = []

for book, cnt in bestsellers:               # bestsellers의 가장 마지막 값(가장 큰 값)과 비교해서 같은 수의 책이 있다면
    if cnt == bestsellers[-1][1]:           # 베스트 셀러 리스트에 추가하기
        bestseller.append(book)

print(sorted(bestseller)[0])                # 가장 많이 팔린 책이 여러개일 경우 사전 순으로 가장 앞의 책제목 출력