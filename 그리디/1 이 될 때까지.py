# n, k
# 1 빼거나, K로 나누거나

n,k = map(int,input().split())
result = 0

while True:
    if n % k == 0:
        n //= k
    else:
        n -= 1
        
    result += 1
    
    if n == 1:
        break
    
print(result)