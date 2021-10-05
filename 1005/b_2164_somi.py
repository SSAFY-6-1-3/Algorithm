N = int(input())
cards = [i for i in range(1, N + 1)] # 1부터 N까지

top = 0            # 가장 맨 위에 있는 카드의 인덱스 번호
bottom = N - 1        # 맨 마지막 인덱스
while top != bottom:  # 1개만 남을때까지
    if top % 2:    # 홀수번 인덱스만 맨 뒤로 추가
        cards.append(cards[top])
        bottom += 1   # 맨 마지막 인덱스
    top += 1        # 맨 위에 있을 카드의 인덱스 번호

print(cards[bottom])


