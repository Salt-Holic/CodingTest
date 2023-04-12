def solution(clothes):
    wear = {}
    for cloth, wearing in clothes:
        if wearing not in wear:
            wear[wearing] = 1
            continue
        wear[wearing] += 1

    answer = 1
    for v in wear.values():
        answer *= v + 1

    return answer - 1