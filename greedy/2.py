# Q) 1이 될 때까지

n, k = map(int , input("plz type n and k: ").split())

cnt = 0

while n != 1:
    if n % k == 0:
        if k == 1:
            n -= 1
            cnt += 1
            continue
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)