# 퀵 정렬
# 피봇 사용
# 시간 복잡도 평균 O(NlogN), 최악 O(N**2)

#### list_comprehension 사용####
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    rest = array[1:]
    
    left = [i for i in rest if i <= pivot]
    right = [i for i in rest if i > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)
    
print(quick_sort(array))



####일반적 풀이#####

# x = [5,7,9,0,3,1,6,2,4,8]

# def quick_sort(x, start, end):
#     if start >= end:
#         return # 원소가 1개 일 때
        
#     pivot = start
#     left = start + 1
#     right = end
    
#     while left <= right:
#         # 피봇보다 작은 left 값을 찾을 때까지
#         while left <= end and x[left] <= x[pivot]:
#             left += 1
#         # 피봇보다 큰 right 값을 찾을 때까지
#         while right > start and x[right] >= x[pivot]:
#             right -= 1
        
#         if left > right: # 엇갈렸다면, 피벗과 교체
#             x[right], x[pivot] = x[pivot], x[right]
#         else: # 아니면 오른쪽과 왼쪽 교체
#             x[left], x[right] = x[right], x[left]
        
#     quick_sort(x, start, right-1)
#     quick_sort(x, right+1, end)

# quick_sort(x, 0, len(x)-1)
# print(x)