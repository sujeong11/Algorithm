def solution(t, p):
    cnt = 0
    t_len, p_len = len(t), len(p)
    
    for i in range(t_len - p_len + 1):
        x = t[i:p_len+i]
        if int(x) <= int(p):
            cnt += 1
    
    return cnt
