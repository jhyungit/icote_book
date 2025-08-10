def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
# 노드 수, 간선 수
v,e = map(int,input().split())

parent = [i for i in range(v+1)] 

answer = 0
edges = []

for _ in range(e):
    node1, node2, cost = map(int,input().split())
    edges.append((node1,node2,cost))

edges.sort(key = lambda x : x[2])

for node1, node2, cost in edges:
    if find_parent(parent, node1) != find_parent(parent, node2):
        print(cost)
        union_parent(parent, node1, node2)
        answer += cost

print(answer)

# 입력 값
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

# 159 출력