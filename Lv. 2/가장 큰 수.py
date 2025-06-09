def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda num: num * 3, reverse=True)
  
    return str(int(''.join(str_numbers)))
