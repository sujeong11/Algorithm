def solution(k, score):
    answer = []
    honor = []
    
    for idx, val in enumerate(score):
        if idx < k:
            honor.append(val)
        else:
            honor_min_val = min(honor)
            if honor_min_val < val:
                honor.remove(honor_min_val)
                honor.append(val)
        
        answer.append(min(honor))
    
    return answer
