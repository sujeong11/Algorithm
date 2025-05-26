def solution(new_id):
    # [1단계]
    new_id = new_id.lower()

    # [2단계]
    for w in new_id:
        if not w.isalpha() and not w.isdigit() and w not in ['-', '_', '.']:
            new_id = new_id.replace(w, '')
    
    # [3단계]
    new_id = list(new_id)
    
    for i in range(len(new_id) - 1):
        if new_id[i] == '.':
            idx = i + 1
            while idx < len(new_id) and new_id[idx] == '.':
                new_id[idx] = ''
                idx += 1

    # [4단계]
    if new_id[0] == '.':
        new_id[0] = ''
    if new_id[-1] == '.':
        new_id[-1] = ''
    
    # [5단계]
    new_id = list(''.join(new_id))
    
    if len(new_id) == 0:
        new_id.append('a')
    
    # [6단계]
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id.pop()
    
    # [7단계]
    while len(new_id) < 3:
        new_id.append(new_id[-1])
    
    return ''.join(new_id)
