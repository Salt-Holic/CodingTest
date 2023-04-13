def solution(genres, plays):
    answer = []
    album = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in album:
            album[genre] = album[genre] + [(play, i)]
            continue
        album[genre] = [(play, i)]

    for v in sorted(album.items(), key=lambda x: -sum(i[0] for i in x[1])):
        for i in sorted(album[v[0]], key=lambda x: -x[0])[:2]:
            answer.append(i[1])
    return answer