def solution(s):
    answer = []
    
    for idx, val in enumerate(s):
        x = s[:idx]
        find_idx = x.rfind(val)
      
        if find_idx == -1:
            answer.append(-1)
        else:
            answer.append(idx - find_idx)
    
    return answer
