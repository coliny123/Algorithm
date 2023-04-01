n = 5
"""
1 - 2 - 5
  - 3 - 4
    DFS와 BFS의 차이는 결국 먼저 들어간 것이 먼저 나오게 할 것인가, 나중에 나오게 할 것인가로 구현
"""
# 6*6의 행렬 만들기 -> 각 0번째 idx 사용을 안할 것임
matrix = [[0]*(n+1) for _ in range(n+1)]

matrix[1][2] = 1
matrix[2][1] = 1

matrix[1][3] = 1
matrix[3][1] = 1

matrix[3][4] = 1
matrix[4][3] = 1

matrix[2][5] = 1
matrix[5][2] = 1

print(matrix)
visited = [False]*(n+1)     # 방문 했으면 True / 안했으면 False를 저장


def DFS(matrix, idx, visited):  # Tree = matrix / 탐색을 시작 하는 지점 = idx / 방문 여부 확인 위한 list = visited
    stack = [idx]   # 맨처음 들어온 노드를 스택에 넣어줌
    visited[idx] = True     # 이 노드를 방문 했다고 기록

    while stack:    # stack이 빌 때까지 반복
        current = stack.pop()   # 맨 처음 입력된 노드가 pop됨
        if not visited[current]:    # 이 노드의 방문 여부 확인
            print(current)      # 현재 노드가 visited 리스트에 방문 되어있지 않으면 출력
            visited[current] = True     # visited 리스트에 방문 했다고 바꿔줌

        # 이제 자식 노드 방문, matrix 구현이라서 idx 가져와야 함
        # 맨 앞 0번 idx는 탐색 x니까 end를 -1로, stack이라 마지막이 먼저 나와서 뒤에서 앞으로 탐색
        for child in range(len(matrix[current])-1, -1, -1):
            if matrix[current][child] == 1 and not visited[child]:  # matrix에 1로 연결 됐는지 확인, 방문 안했는지 확인
                stack.append(child)


print("DFS result")
DFS(matrix, 1, visited)


from collections import deque
def BFS(matrix, idx, visited):
    queue = deque()
    queue.append(idx)

    while queue:        # queue가 다 없어질 때까지 반복
        current = queue.popleft()

        if not visited[current]:
            print(current)
            visited[current] = True

        for child in range(len(matrix[current])):   # 연결된 모든 노드들이 나오게 됨
            if matrix[current][child] == 1 and not visited[child]:  # 인덱스로 나온 노드와 현재 노드가 부모 자식관계인지 확인, 방문했는지 확인
                queue.append(child)


visited = [False]*(n+1)     # 초기화
print("BFS result")
BFS(matrix, 1, visited)



