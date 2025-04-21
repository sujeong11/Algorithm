def solution(n, m):
    gcd, lcm = 0, n * m
    
    while m:
        r = n % m
        n, m = m, r
    
    gcd = n
    lcm /= gcd
    
    return [gcd, lcm]
