num = int(input())
count = 0
n_sum = 0
for i in range(1,200):
    n_sum += i
    if (num - n_sum) > i:
        count += 1
    else:
        count += 1
        break
print(count)
