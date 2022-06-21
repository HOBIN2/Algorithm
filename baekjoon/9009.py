def fibona(n):
    if n >= 3: 
        return fibona(n-1) + fibona(n-2)
    else:
        return 1
N = int(input())
for i in range(N):
    x = int(input())
    n = 1
    fibona_list = []
    while x:
        if x < fibona(n):
            fibona_list.append(fibona(n-1))
            x -= fibona(n-1)
            n = 0
        n += 1
    
    print(sorted(fibona_list))