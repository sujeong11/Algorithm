def solution(s):
    answer = []
    words = s.split(" ")
    
    for word in words:
        new_word = ""
        
        for idx in range(len(word)):
            if idx % 2 == 0:
                new_word += word[idx].upper()
            else:
                new_word += word[idx].lower()
        
        answer.append(new_word)

    return " ".join(answer)
