def solution(food_times, k):
    answer = 0
    time = 0
    while time != k:
        for i in range(len(food_times)):
            if food_times[i] == 0:
                continue
            else:
                food_times[i] -= 1
                time += 1
    for j in range(len(food_times)):
        if sum(food_times) == 0:
            answer = -1
            break
        elif food_times[j] != 0:
            answer = j + 1
            break

    return answer
print(solution([3,1,2],5))
#시간초과..