def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for w in word:
            if w * 2 not in b:
                # 한 칸의 공백으로 바꾸지 않으면 기존 문장 구조가 깨짐 (떨어져 있던 단어들이 붙게되므로)
                b = b.replace(w, " ")
            
        if not b.replace(" ", ""):
            answer += 1

    return answer
