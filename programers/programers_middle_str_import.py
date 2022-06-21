#int와 round쓰지말기
def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        find = len(s) // 2
        answer = s[find-1:find+1]
    else:
        answer = s[len(s)//2]
    return answer