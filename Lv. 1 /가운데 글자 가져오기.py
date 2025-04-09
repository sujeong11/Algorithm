def solution(s):
    len_s = len(s)
    mid = len(s) // 2
    
    if len_s % 2 ==0:
        return s[mid-1:mid+1]
    
    return s[mid]
