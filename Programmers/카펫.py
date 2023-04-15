def solution(brown, yellow):
    size = brown + yellow
    data = []

    for i in range(1, size + 1):
        if size % i == 0:
            data.append(i)

    for i in data:
        h = i
        w = size / h
        if (w - 2) * (h - 2) == yellow:
            return [w, h]

    '''
    if size % 2 == 0:
        return [data[int(len(data)*0.5)], data[int(len(data)*0.5)-1]]

    return data[int(len(data)*0.5):int(len(data)*0.5)+1]*2
    '''