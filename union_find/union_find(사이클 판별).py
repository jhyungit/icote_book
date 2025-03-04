def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return parent
    

n,v = 3, 3 # 노드 수, 간선 수

v = [(1,2),(2,3),(1,3)]
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i # 부모노드 초기화

cycle = False

for a,b in v:
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)

print(cycle)