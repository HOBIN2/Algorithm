N = input()
a = 10
x = (len(N) // a) + 1
for i in range(x):
    print(N[a*i:a*(i+1)])

