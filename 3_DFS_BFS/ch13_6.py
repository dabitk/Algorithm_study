n = int(input())

board = []
teacher_positions = [] # (x, y) 형태로 선생들 위한 좌표 저장. 
free_positions = [] # 장애물을 설치할 수 있는 위치들 좌표 저장

flag = False # 마지막 결과 출력용 플래그. True면 장애물 3개 설치한 상태에서 모든 선생들이 학생을 발견하지 못한 경우 

for i in range(n):
    board.append(list(input().split()))

def check(t_positions):
    global n, board
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    teacher_x = t_positions[0]
    teacher_y = t_positions[1]
    

    for i in range(4): # 4가지 방향으로 하나씩 체크
        new_x = teacher_x + dx[i]
        new_y = teacher_y + dy[i]
        if new_x > 0 and new_y > 0 and new_x < n and new_y < n: # 보드를 벗어나지 않는 범위인지 체크
            if board[new_x][new_y] == 'O': # 장애물에 부딫히면 이 방향으로 탐색은 종료
                break
            elif board[new_x][new_y] == 'X': # 학생 발견 시 '선생이 학생을 볼 수 있음'으로 true
                return True

            


def dfs(obstacle_num, idx):
    global flag
    if obstacle_num == 3:
        for i in teacher_positions:
            if check(i):
                flag = False
                return
            
        # 장애물 3개 설치한 상태에서 모든 선생들이 학생을 발견하지 못한 경우 
        flag = True
        return

    for x in free_positions[idx:]:
        board[x[0]][x[1]] = 'O' # 장애물이 없는 곳에 장애물을 일단 설치하고
        dfs(obstacle_num + 1, idx + 1) # 재귀호출 후
        board[x[0]][x[1]] = 'X' # 다시 원복한다. 
        
        #이런식으로 재귀함수 호출 전에 무언갈 하고 재귀함수 호출 후에 했던 무언간 원복시키는 유형의 문제를 '백트래킹' 유형이라고 함.




for i in range(n):
    for j in range(n):
        if board[i][j] == 'T':
            teacher_positions.append((i, j))
        elif board[i][j] == 'X':
            free_positions.append((i, j))


dfs(0, 0)
if flag:
    print('YES')
else:
    print('NO')