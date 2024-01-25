# 삽입 정렬
# 시간 복잡도 O(N**2), 최선 O(N)

x = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(x)):
    for j in range(i, 0, -1):
        if x[j] < x[j-1]:
            x[j-1], x[j] = x[j], x[j-1]

print(x)