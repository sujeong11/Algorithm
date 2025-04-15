def solution(price, money, count):
    flag = 1
    
    for i in range(count):
        money -= (price * flag)
        flag += 1
        
    if money > 0:
        return 0
    else:
        return -money
