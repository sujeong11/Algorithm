def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    return [sum(dic.get(person, 0) for person in group) for group in photo]
