import math
T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())
    if (N % H) == 0:
        floor = str(H)
    else:
        floor = str(N % H) 
    room  = str(math.ceil(N/H))
    if len(room) == 1:
        room = '0' + room
    room_num = int(floor + room)
    print(room_num)