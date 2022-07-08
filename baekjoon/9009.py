T = int(input())
fibonacci_list = [0,1]

for _ in range(T):
    goal_sum = int(input())
    n = 1
    factor_list = []
    while goal_sum:
        
        if goal_sum >= fibonacci_list[-1]:
            factor = fibonacci_list[-2] + fibonacci_list[-1]
            fibonacci_list.append(factor)
        n +=1            
        if goal_sum < fibonacci_list[n]:
            factor_list.append(fibonacci_list[n-1])
            goal_sum -= fibonacci_list[n-1]
            n = 1    
    print(*sorted(factor_list))        
                        