# Q) 왕실의 나이트

col = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
move = [[2,-1],[2,1],[-2,-1],[-2,1],[1,-2],[-1,-2],[1,2],[-1,2]] # RU, RD, LU, LD, UR, UL, DR, DL

start = list(input('말의 위치 입력 ex) a1 : '))
cnt = 0

for dx, dy in move:
    if int(start[1]) + dx in range(1,9) and col[start[0]] + dy in range(1,9):
        cnt += 1
    
print(cnt)