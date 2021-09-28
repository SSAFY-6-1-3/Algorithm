def min_heap(scovile):
    heap = [0, scovile[0]]
    for i in range(1, len(scovile)):
        heap.append(scovile[i])
        if heap[i+1] <= heap[i+1 // 2]:
            idx = i+1
            while heap[idx] <= heap[idx // 2]:
                if idx == 1:
                    break
                heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
                idx //= 2

    return heap[1:]


answer = 0


def solution3(scovile, K):
    global answer
    scovile = min_heap(scovile)
    if len(scovile) == 1 and scovile[0] < K:
        return -1
    if scovile[0] >= K:
        return answer
    num1 = scovile.pop(0)
    scovile = min_heap(scovile)
    num2 = scovile.pop(0)
    new_scov = num1 + num2 * 2
    scovile.append(new_scov)
    scovile = min_heap(scovile)
    answer += 1
    return solution3(scovile, K)


print('\n' + '-' * 50 + '\n')
print(solution3([2, 1, 3, 9, 10, 12], 7))
print('\n' + '-' * 50 + '\n')
print(solution3([1, 2, 9], 7))
print('\n' + '-' * 50 + '\n')
print(solution3([1, 1, 1, 1, 1, 1, 30], 20))
print('\n' + '-' * 50 + '\n')
print(solution3([1, 1, 1], 8))
print('\n' + '-' * 50 + '\n')
print(solution3([3, 5, 7, 23, 1, 2, 8], 35))
print('\n' + '-' * 50 + '\n')
print(solution3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 2, 2, 2, 8], 70))
