from string import ascii_lowercase
S = input()
alpha_list = list(ascii_lowercase)
count_list = [0] * len(alpha_list)
for i in S:
    if i in alpha_list:
        count_index = alpha_list.index(i)
        count_list[count_index] += 1
print(*count_list)

