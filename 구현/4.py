# Q) 문자열 재정렬

x = input('문자열 입력 : ')
digit = [str(i) for i in range(10)] # 0~9

x_list = list(x)
num = 0
alpha = []

for i in x_list:
    if i in digit:
        num += int(i)
    else:
        alpha.append(i)
alpha.sort()
alpha.append(str(num))

print(''.join(alpha)) # 리스트를 스트링으로 변환할 때, ''.join(리스트명) 사용!