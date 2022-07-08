x_list = []
y_list = []
for i in range(3):
    x, y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)
for i,j in zip(x_list,y_list):
    if x_list.count(i) == 1:
        x = i
    if y_list.count(j) == 1:
        y = j
print(x,y)
