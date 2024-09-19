from collections import deque

n, k = map(int, input().split())

map_data = []
virus_position = []

for i in range(n):
    map_data.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

for i in range(n):
    for j in range(n):
        if map_data[i][j] != 0:
            virus_position.append((map_data[i][j], [i, j], 0)) # 바이러스 값, 바이러스 좌표, 시간


virus_position.sort()

dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]

q = deque(virus_position) # deque에서는 sort가 없다고 해서 리스트로 오름차순 정렬 수 deque 변환

while q:
    current = q.popleft()
    curr_x, curr_y = current[1][0], current[1][1]
    curr_time = current[2]
    if curr_time == s+1:
        break
    
    for i in range(4):
        dx, dy = curr_x + dir_x[i] , curr_y + dir_y[i]
        if dx < 0 or dy < 0 or dx >= n or dy >= n or map_data[dx][dy] != 0: # 맵 범위 벗어나거나 이미 바이러스가 퍼진 패널인 경우 암것도 안함
            continue
        map_data[dx][dy] = current[0] # 위 아래 왼쪽 오른쪽 위치 바이러스 전파
        virus_position.append((current[0], [dx, dy], curr_time + 1))

print(map_data[x-1][y-1])

