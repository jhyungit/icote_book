# 계수 정렬
# 시간/공간 복잡도 O(N+K)

x = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
index = [i for i in range(max(x)+1)]
cnt = [0] * (max(x) + 1)

for i in x:
    cnt[i] += 1

for i in range(len(cnt)):
    print(f'{i} ' * cnt[i], end = '')