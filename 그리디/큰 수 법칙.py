# n, m, k
# m 번 더하여 가장 큰 수
# k 번 연속해서 못 더함

n,m,k = map(int, input().split())
arr = list(map(int, input().split()))
new_k = k
answer = 0
arr.sort(reverse=True)

for i in range(m):
    if k:
        answer += arr[0]
        k-=1
    else:
        answer += arr[1]
        k = new_k

print(answer)