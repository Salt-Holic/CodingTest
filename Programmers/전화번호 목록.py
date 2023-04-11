def solution(phone_book):
    if len(phone_book) == 1:
        return True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            return False

    return True