# # map함수를 이용한 input 여러개 받기
# map(함수, 튜플 or 리스트와 같은 iterable한 자료형)
# a, b = map(int, input('숫자 두 개를 입력하세요: ').split(',')) # 입력받은 값을 콤마를 기준으로 분리
# print(a + b)
n, m = map(int, input().split())
# print(n,m)
a, b, c = map(int, input().split())
print(a,b,c)


# # 튜플 삽입
# list = [a,b,c]
# t = tuple(list[i] for i in range(len(list)))
# print(t)

# 2차원 배열 선언
column, row = 3, 5
array2D = [[i for i in range(column)] for _ in range(row)] # 0으로 3X5 배열 생성
print(array2D)
A = [[0]*column for _ in range(row)]
print(A) # array2D와 같다.
for i in array2D:
	print("행 :", i)

num = [1,2,3,4,5]

# 배열 초기화 방법
a = [0] * len(num)
a = [0 for _ in range(len(num))]

#그래프 입력받기
N = 10
graph = []
for i in range(N):
	graph.append(list(map(int,input())))