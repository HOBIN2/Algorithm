N = input()
length = len(N)
length_half = int(length / 2) 
left = 0
right = 0

for x in range(length_half):
    left += int(N[x])
for y in range(length_half,length):
    right += int(N[y])

if left == right:
    print("LUCKY")
else:
    print("READY")