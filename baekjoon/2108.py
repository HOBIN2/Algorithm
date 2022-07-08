from collections import Counter
import sys
N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()
print((round((sum(num_list)/N))))
print(num_list[(N//2)])
num_count = Counter(num_list).most_common(2)
if len(num_count) >= 2:
    if num_count[0][1] > num_count[1][1]:
        print(num_count[0][0])
    else: 
        print(num_count[1][0])
else:
    print(num_count[0][0])
print(num_list[-1] - num_list[0]) 