num_dict = {"zero": "0", "one": "1", "two": "2","three": "3", "four": "4", "five": "5","six": "6","seven": "7", "eight": "8", "nine": "9"}

def solution(s):    
    for i in num_dict:
        s = s.replace(i, num_dict.get(i))
    
    return int(s)