def solution(a, b, n):
    answer = 0
    
    while n >= a:
        new_bottle_cnt = n // a
        answer += (new_bottle_cnt * b)
        n = n - (new_bottle_cnt * a) + (new_bottle_cnt * b)

    return answer
