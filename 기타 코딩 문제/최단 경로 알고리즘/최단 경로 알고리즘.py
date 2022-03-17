'''
다익스트라 최단 경로 알고리즘
- 음의 간선이 없을 때 정상적으로 동작합니다.
- 그리디 알고리즘으로 분류됩니다.
  - 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복합니다.

알고리즘의 동작과정
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 3, 4를 반복

다익스트라 알고리즘 특징
- 그리디 알고리즘: 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복합니다.
- 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않습니다.
  - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있습니다.
- 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장됩니다.
  - 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 합니다.

다익스트라 알고리즘 구현
단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인(순차 탐색)합니다.

총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 합니다. -> V는 노드의 개수
따라서 전체 시간 복잡도는 O(V^2)입니다.
일반적으로 코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5000개 이하라면 이코드로 문제를 해결할 수 있습니다. -> 1초에 2천만번 정도의 연산이 처리된다면 합리적이다.
  - 하지만 노드의 개수가 10000개를 넘어가는 문제라면 어떻게 해야 할까요?

우선순위 큐
우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조입니다.
예를 들어 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우에 우선순위 큐를 이용할 수 있습니다.
Python, C++, Java를 포함한 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원합니다.
우선순위 큐의 추출되는 데이터 -> 가장 우선순위가 높은 데이터

힙
우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나입니다.
최소 힙과 최대 힙이 있습니다.
다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용됩니다.

우선순위 큐 구현 방식
리스트 : 삽입시간 O(1) 삭제시간 O(N)
힙: 삽입시간 O(logN) 삭제시간 O(logN)

단계마다 방문하지 않은 노드 중에서 최단 거리가 짧은 노드를 선택하기 위해 힙(Heap) 자료구조를 이용합니다.
다익스트라 알고리즘이 동작하는 기본 원리는 동일합니다.
  - 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조를 추가적으로 이용한다는 점이 다릅니다.
  - 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용합니다.

힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 O(ElogV)입니다.
노드를 하나씩 꺼내 검사하는 반복문은 노드의 개수 V이상의 횟수로는 처리되지 않습니다.
- 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 최대 간선의 개수(E)만큼
연산이 수행될 수 있습니다.
직관적으로 전체과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내느 ㄴ연산과 매우 유사합니다.
- 시간 복잡도를 O(ElogE)로 판단할 수 있습니다.
- 중복 간선을 포함하지 않는 경우에 이를 O(ElogV)로 정리할 수 있습니다.
  - O(logE)-> O(ElogV^2) -> O(2ElogV) -> O(ElogV)
'''
import math

INF = math.inf

n,m = map(int, input("노드의 개수, 간선의 개수를 입력하기 : ").split())
start = int(input("시작 노드를 입력해주세요 : "))
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)


# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input("간선 정보를 입력해주세요").split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 최단 거리가 가장 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]: # 시작 노드와 연결된 노드의 최단 거리 테이블 초기화
        distance[j[0]] = j[1]
    
    # 시작 노드를 제외한 전체 n-1개의 노드에 대한 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost <distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달 할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("무한")
    else:
        print(distance[i])

# 힙을 이용한 다익스트라 알고리즘-----------------------------------

import heapq
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

def dijkstra_heap(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start)) # (리스트, (우선순위, 값))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]] : 
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra_heap(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달 할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("무한")
    else:
        print(distance[i])