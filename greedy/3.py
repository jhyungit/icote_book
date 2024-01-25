# Q) 곱하기 혹은 더하기

s = input("plz type s : ")
answer = 0

for i in s:
    if int(i) <= 1 or answer == 0:
        answer += int(i)
    else:
        answer *= int(i)
            
print(answer)