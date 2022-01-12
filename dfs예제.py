def dfs(graph,v,visited): #O(N) time
  visited[v]=True
  print(v,end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited) #사실상 dfs 알고리즘 코드 끝

graph=[ #인접리스트 방식 (not 인접 행렬)
  [], #0번 노드 자리, 실제론 없음.
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7] #8번 노드 자리
]

visited = [False]*9 #노드번호 (0~8)

dfs(graph,1,visited)



