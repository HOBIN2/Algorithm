a = list(range(1,4001))
print(500000/4000)
from collections import Counter
import time
N = 500000
num_list = a * 125
# for _ in range(N):
#     num_list.append(int(input()))
start_time = time.time()
num_list.sort()
print((round((sum(num_list)/N))))
print(num_list[(N//2)])
num_count = Counter(num_list).most_common(2)
if num_count[0][1] > num_count[1][1]:
    print(num_count[0][0])
else: 
    print(num_count[1][0])
print(num_list[-1] - num_list[0]) 
end_time = time.time()
print(end_time-start_time)
