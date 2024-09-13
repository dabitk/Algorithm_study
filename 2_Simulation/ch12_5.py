from collections import deque

# ================= 초기 세팅 ============

N = int(input())
K = int(input())

board = [[0] * (N) for _ in range(N)]
apple_map = [[0] * (N) for _ in range(N)]


for i in range(K):
    apple_x, apple_y = map(int, input().split())
    apple_map[apple_x][apple_y] = 2 # 사과는 2, (뱀은 board에 표시) 뱀은 1, 아무것도 없으면 0

L = int(input()) # 뱀 방향 전환 횟수

move_dict = {}
for i in range(L):
    move_time, move_dir = input().split()
    move_dict[move_time] = move_dir

# 앞뒤로 원소 추가 제거가 자유로운 deque로 뱀 구성. 뱀은 좌표로 구성되어있음.
snake = deque([[0, 0]]) # NOTE: list를 원소로 가진 deque를 만들기 위해 대괄호 2개임
board[0][0] = 1 # 보드 상의 뱀의 시작 위치. 라인13에 나왔듯이 1은 뱀을 의미함

current_time = 0 # 게임 시작 후 지난 시간.
direction = 0 # 정수형 뱀의 이동 방향. (동, 서, 남, 북). 처음 시작 방향은 동부터 시작 (문제 지문:"뱀은 처음에 오른쪽을 향합니다")



# ================= 게임 로직 ============
def move():
    # 동 북 서 남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    global snake, direction, board, apple_map, move_dict, current_time # 전역변수 snake에 접근 가능하게 하는 파이썬 키워드

    snake_head = snake[0]

    snake_head_new = [snake_head[0] + dx[direction], snake_head[1] + dy[direction]]
    # print('direction', direction)
    # print('snake_head_new', snake_head_new)

    # 뱀 이동 가능 여부 체크
    if check(snake_head_new) == True: # True면 게임 속행, False면 게임오버
        snake.appendleft(snake_head_new) # 뱀 머리가 새로 이동한 좌표를 뱀에 더한다
        board[snake_head_new[0]][snake_head_new[1]] = 1; # 보드에도 뱀이 이동한 위치에 뱀 표시(1) 추가
    else:
        return False # 게임오버
    
    # 사과 여부 체크
    if apple_map[snake_head_new[0]][snake_head_new[1]] == 2:
        apple_map[snake_head_new[0]][snake_head_new[1]] = 0 # 시과를 먹었으므로 0으로 변경
    else:
        snake_tail = snake.pop() # deque에서 마지막 (맨 오른쪽) 추출
        board[snake_tail[0]][snake_tail[1]] = 0 # 보드에서도 뱀의 꼬리 부분 삭제 (=사과가 없어서 뱀이 몸통 길이가 그대로인채로 이동해서 1칸 만큼 기존 꼬리 위치가 0으로 됨)


    # print(current_time)
    print(move_dict)

    # 방향 전환
    if str(current_time) in move_dict:
        if move_dict[str(current_time)] == 'D': # 오른쪽으로 전환
            print('curr D', current_time)
            direction -= 1
            if direction == -1:
                direction = 3
        else: # 왼쪽으로 전환
            print('curr L', current_time)
            direction += 1
            if direction == 4:
                direction = 0


    return True

    


def check(snake_head_new):
    global board
    new_x, new_y = snake_head_new

    if new_x < 0 or new_y < 0 or new_x > len(board) - 1 or new_y > len(board[0]) - 1 : # 새 이동 위치가 보드 범위를 벗어난 경우
        return False

    if board[new_x][new_y] == 1: # 새 이동 위치에 뱀 (의 몸통)이 있는 경우 게임오버
        return False
    
    # print('here')
    return True




# ================= 여기서 부터 실제 게임 시작 ============
flag = True
while flag:
    current_time += 1
    flag = move()

    for i in board:
        print(i)
    print('================')
    
print(current_time) # 게임이 끝난 시점의 시간을 출력