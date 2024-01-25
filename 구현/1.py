# 구현 : 알고리즘을 코드로 바꾸는 과정
# 풀이는 쉽지만, 소스코드 구현은 어려운 것들
# 순열 등 itertools 참고

# Q) 상하좌우
n = int(input("이동할 횟수 입력 : "))
direction = list(input('이동할 방향 입력 : ').split())

start = [1,1]
move = {'R' : [0,1], 'L' : [0,-1], 'U' : [-1,0], 'D' : [1,0]}

for i in direction:
    start[0] = start[0] + move[i][0]
    start[1] = start[1] + move[i][1]
    if start[0] < 1 or start[1] < 1 or start[0] > n or start[1] > n:
        start[0] = start[0] - move[i][0]
        start[1] = start[1] - move[i][1]
print(start)