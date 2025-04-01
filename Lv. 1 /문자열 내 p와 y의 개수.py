def solution(s):
    s = s.lower()
    
    count_p = s.count('p')
    count_y = s.count('y')
    
    if count_p == count_y:
        return True
    elif count_p != count_y:
        return False
    else:
        return True
