from itertools import combinations

def is_Prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    num_sum_arr = [sum(n) for n in combinations(nums, 3)]
    
    for i in num_sum_arr:
        if is_Prime(i):
            answer += 1
    
    return answer
