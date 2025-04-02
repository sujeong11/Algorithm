def solution(n):
    list_num = list(str(n))
    list_num.sort(reverse=True)
    return int("".join(map(str, list_num)))
