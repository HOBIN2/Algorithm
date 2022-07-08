N = int(input())
for i in range(-N+1,N):
    print(' '*(N-1-(abs(i))) + '*' * (abs(i)*2 +1))