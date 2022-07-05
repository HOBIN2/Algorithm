x, y = map(int,input().split())
week = ['SUN','MON','TUE','WED', 'THU', 'FRI', 'SAT']
d31 = [1,3,5,7,8,10,12]
d30 = [4,6,9,11]
sum = 0
for i in range(1,x):
    if i in d31:
        sum += 31
    elif i in d30:
        sum += 30
    else: 
        sum += 28
sum += y
print(week[sum%7])