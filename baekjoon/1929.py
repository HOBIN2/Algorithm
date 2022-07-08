x, y = map(int,input().split())
# import time
# start_time = time.time()
# x = 1
# y = 1000000
count = 0
for a in range(x,y+1):
    if a == 1:
            continue
    for b in range(1,int(a**0.5)+1):
        if  a % b == 0:
            count += 1
            if count == 2:
                break
    if count == 1:
        print(a)
    count = 0       
# end_time = time.time()
# print((end_time-start_time))
    