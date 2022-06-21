array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []
for i in commands:
    result = array[i[0]-1:i[1]]
    result.sort()
    answer.append(result[i[2]-1])
print(answer)