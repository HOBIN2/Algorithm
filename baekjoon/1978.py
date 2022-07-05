N = int(input())
num_list = list(map(int,input().split()))
count = 0
for x in num_list:
    if x == 1:
        continue
    num_count = 0
    for y in range(2,x):
        if x % y == 0:
            num_count += 1
    if num_count == 0:
        count += 1
print(count)
