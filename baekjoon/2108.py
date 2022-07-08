a = [-1,5,1,1,2,2,3,4]
b = sorted(list(set(a)))
count_list = []
for i in b:
    count_list.append(a.count(i))
print(count_list)
print(b)
max_a = max(count_list)
