a = [4,7,12]
b = [True,False,True]
answer = 0
for i in range(len(a)):
    if b[i]:
        a[i] = a[i]
    else:
        a[i] = -a[i]
answer = sum(a)
print(answer)
