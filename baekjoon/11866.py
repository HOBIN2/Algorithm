N, K = map(int,input().split())
queue_list = list(range(1,N+1))
jose_list = []
count = 0
while queue_list:
    factor = queue_list.pop(0)
    if count == K-1:
        jose_list.append(str(factor))
        count = 0 
    else:
        queue_list.append(factor)
        count += 1

print('<',', '.join(jose_list),'>', sep="")
