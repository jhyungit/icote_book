# Q) 거스름돈

N = 1260
x = [500, 100, 50, 10]

cnt = 0
for i in range(len(x)):
    cnt += N // x[i]
    N %= x[i]

print(cnt)