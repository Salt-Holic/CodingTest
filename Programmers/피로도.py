from itertools import permutations


def solution(k, dungeons):
    adventure_score = []

    for dungeon in permutations(dungeons, len(dungeons)):
        current_k = k
        cnt = 0
        for d in dungeon:
            if current_k >= d[0]:
                current_k -= d[1]
                cnt += 1
            continue
        adventure_score.append(cnt)

    return max(adventure_score)