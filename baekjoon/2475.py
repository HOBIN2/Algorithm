num_list = list(map(int,input().split()))
n_sum = 0
for i in num_list:
    n_sum += (i ** 2)
print(n_sum % 10)