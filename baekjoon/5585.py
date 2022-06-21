N = int(input())
change_list = [500,100,50,10,5,1]
change = 1000 - N
count = 0
for i in change_list:
    if change == 0:
        break
    elif (change // i) >= 1:
        count += change // i
        change = change % i
print(count)