N = int(input())
fibonacci_list = [0,1]
if N <= 1:
    print(fibonacci_list[N])
else:
    for i in range(N-1):
        factor = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(factor)
    print(fibonacci_list[N])