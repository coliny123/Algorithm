n = 5
"""
1 - 2 - 5
  - 3 - 4
  
  DFS와 BFS의 차이는 결국 먼저 들어간 것이 먼저 나오게 할 것인가, 나중에 나오게 할 것인가로 구현
"""
graph = [[] for _ in range(n+1)]

graph[1] = [2, 3]
graph[2] = [5]
graph[3] = [4]
graph[4] = []
graph[5] = []

print(graph)
visited = [False]*(n+1)     # 방문 했으면 True / 안했으면 False를 저장


def DFS(graph, idx, visited):  # Tree = matrix / 탐색을 시작 하는 지점 = idx / 방문 여부 확인 위한 list = visited
    stack = [idx]   # 맨처음 들어온 노드를 스택에 넣어줌
    visited[idx] = True     # 이 노드를 방문 했다고 기록

    while stack:    # stack이 빌 때까지 반복
        current = stack.pop()   # 맨 처음 입력된 노드가 pop됨
        if not visited[current]:    # 이 노드의 방문 여부 확인
            print(current)      # 현재 노드가 visited 리스트에 방문 되어있지 않으면 출력
            visited[current] = True     # visited 리스트에 방문 했다고 바꿔줌

        # 현재 노드의 자식 노드가 리스트로 반환됨
        for child in graph[current]:
            if not visited[child]:
                stack.append(child)


print("DFS result")
DFS(graph=graph, idx=1, visited=visited)    # stack 이니까 먼저 들어간 2가 나중에 나오고 3이, 4가 먼저 들어갔지만 5가 먼저 나옴


from collections import deque
def BFS(graph, idx, visited):
    queue = deque()
    queue.append(idx)

    while queue:        # queue가 다 없어질 때까지 반복
        current = queue.popleft()

        if not visited[current]:
            print(current)
            visited[current] = True

        for child in graph[current]:
            if not visited[child]:
                queue.append(child)


visited = [False]*(n+1)     # 초기화
print("BFS result")
BFS(graph, 1, visited)
