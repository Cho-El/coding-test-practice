'''
알고리즘의 구현에 있어서 행렬에 대한 이해는 필수적이다.
행(row) 열(column)은 보통 각각 x,y로 지칭하며
행은 상하로 이동, 열은 좌우로 이동한다
'''
# 행렬 소스코드 구현

# 동, 북, 서, 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 현재 위치
x, y = 2, 2

for i in range(4):
	# 다음 위치
	nx = x + dx[i]
	ny = y + dy[i]

	print(nx, ny)