def solution(lottos, win_nums):
    answer = []
    count = 0
    rank = [6,6,5,4,3,2,1]
    for i in lottos:
        if i in win_nums:
            count += 1
    max = count + lottos.count(0)
    min = count
    answer.append(rank[max])
    answer.append(rank[min])
    return answer
print(solution([44,1,0,0,31,25],[31,10,45,1,6,19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))