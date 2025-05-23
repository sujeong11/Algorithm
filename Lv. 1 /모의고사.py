def solution(answers):
    person1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for idx, answer in enumerate(answers):
        if answer == person1[idx % len(person1)]:
            score[0] += 1
        if answer == person2[idx % len(person2)]:
            score[1] += 1
        if answer == person3[idx % len(person3)]:
            score[2] += 1

    max_score = max(score)
    
    return [idx + 1 for idx, val in enumerate(score) if val == max(score)]
