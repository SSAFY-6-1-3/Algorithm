import sys

input = sys.stdin.readline

def solut(N, nums):
    san = round(sum(nums)/N)
    print(san)

    nums.sort()
    print(nums[N//2])

    if N ==1:
        print(nums[0])
    else:
        dct = {}
        for num in nums:
            if dct.get(num) == None:
                dct[num] = 1
            else:
                dct[num] += 1
        dct_list = sorted(dct.items(), key= lambda x:(-x[1], x[0]))
        if dct_list[0][1] == dct_list[1][1]:
            print(dct_list[1][0])
        else:
            print(dct_list[0][0])

    print(nums[-1] - nums[0])



N = int(input())
nums = [int(input()) for _ in range(N)]
solut(N, nums)