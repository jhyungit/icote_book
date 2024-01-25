# 선택 정렬
# 시간 복잡도 O(N**2)

x = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(x)):
    min_index = i
    for j in range(i+1,len(x)):
        if x[min_index] > x[j]:
            min_index = j
    x[i], x[min_index] = x[min_index], x[i]
print(x)