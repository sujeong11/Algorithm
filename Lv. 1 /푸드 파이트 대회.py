def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        temp = food[i] // 2        
        answer += (str(i) * temp)
    
    return answer + '0' + answer[::-1]
