def solution(answers):
    answer = []

    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for i in range(len(answers)):
        if p1[i % 5] == answers[i]:
            score[0] += 1
        if p2[i % 8] == answers[i]:
            score[1] += 1
        if p3[i % 10] == answers[i]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx + 1)
    return answer
    '''
    n = score.count(max(score))
    print(n)
    print(score)
    if n == 3:
        return [1,2,3]
    if n == 1:
        return [(score.index(max(score)))+1]
    if n == 2:
        if score[0] == score[1]:
            return [1,2]
        if score[0] == score[2]:
            return [1,3]
        if score[1] == score[2]:
            return [2,3]
    '''

    # if len(score) == len(set(score)):
    #    return [(score.index(max(score)))+1]
    # return answer