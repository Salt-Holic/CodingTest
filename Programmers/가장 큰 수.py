def solution(numbers):
    print(sorted(['666', '101010']))
    answer = ''.join(sorted(map(str, numbers), key=lambda x: (x * 3), reverse=True))
    if answer[0] == '0':
        answer = '0'

    return answer