def solution(s, n):
    answer = ''
    
    for alp in s:
        if alp == ' ':
            answer += ' '
            continue
        
        alp_ascii = ord(alp)
        change_ascill = alp_ascii + n
        
        if alp.isupper() and change_ascill > 90:
            answer += chr(65 + (change_ascill - 91))
        elif alp.islower() and change_ascill > 122:
            answer += chr(97 + (change_ascill - 123))
        else:
            answer += chr(change_ascill)
    
    return answer
