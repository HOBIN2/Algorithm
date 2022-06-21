S = list(map(int,input()))
result = S[0]
for i in range(1, len(S)):
    if result <= 1:
        result += S[i]
    elif S[i] > 1:
        result *= S[i]
print(result)

