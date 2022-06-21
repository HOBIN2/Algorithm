import random
win_paper = []
for i in range(10):
    win_num = []
    while True:
        if len(win_num) == 6:
            break
        a = random.randint(1,45)
        if a in win_num:
            continue
        else:
            win_num.append(a)
            win_num.sort()
    win_paper.append(win_num)
for i in win_paper:
    print(i)