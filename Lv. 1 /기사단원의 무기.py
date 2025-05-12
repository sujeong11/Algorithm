def solution(number, limit, power):
    val = []
    
    for i in range(1, number + 1):
        cnt = 0
        
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                cnt += 2 if j != i // j else 1
        
        if cnt > limit:
            val.append(power)
        else:
            val.append(cnt)
    
    return sum(val)
