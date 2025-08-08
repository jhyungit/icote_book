def binary_search(array, target, bottom, top):
    while bottom <= top:
        total = 0
        mid = (bottom+top) // 2
        total = sum((x - mid) for x in array if x > mid)
        
        if total < target:
            top = mid - 1
        else:
            answer = mid
            bottom = mid + 1
    return answer

n,m = map(int,input().split())
array = list(map(int,input().split()))

answer = 0
bottom = 0
top = max(array)
target = m

x = binary_search(array,target,bottom,top)
print(x)