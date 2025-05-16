def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(0, len(score), m):
        if len(score) - i < m:
            break
        min_val = min(score[i:i + m])
        answer += (min_val * m)
    
    return answer
