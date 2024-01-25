# Q) 모험가 길드 문제 조건

n = input("모험가 수 입력: ")
k = list(map(int, input("모험가 별 공포도 입력: ").split()))
k.sort()

new = 0
group = 0

for i in k:
    new += 1
    if new >= i:
        group += 1
        new = 0
print(group)