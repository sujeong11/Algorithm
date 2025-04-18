def solution(arr1, arr2):
    answer = []
    
    for x, y in zip(arr1, arr2):
        temp = []
        for i, j in zip(x, y):
            temp.append(i + j)

        answer.append(temp)
    
    return answer
