def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum_val = sum(months[:a-1]) + b
    
    return days[sum_val % 7 - 1]
