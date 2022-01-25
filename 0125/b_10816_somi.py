N = int(input())
cards = list(map(int, input().split()))
M = int(input())
count_cards = list(map(int, input().split()))


cards_dict = {} #{card : 개수}
for card in cards:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

ans = []
for cnt_card in count_cards:
    if cnt_card in cards_dict:
        ans.append(cards_dict[cnt_card])
    else:
        ans.append(0)

print(*ans)