def solution(n):
    bin_3 = ""
    
    while n != 0:
        quot, div = n // 3, n % 3
        n = quot
        bin_3 += str(div)

    num_3 = bin_3[::-1]

    return sum(((3 ** idx) * int(val)) for idx, val in enumerate(num_3)) 
