K = int(input())
money_list = []
for i in range(K):
    money = int(input())
    if money > 0:
        money_list.append(money)
    elif money == 0:
        money_list.pop(-1)
print(sum(money_list))