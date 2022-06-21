from itertools import combinations
def solution(numbers):
    answer = []

    com = list(combinations(numbers,2))
    for i in com:
        result = sum(i)
        if result not in answer:
            answer.append(result)
    answer.sort()
    return answer