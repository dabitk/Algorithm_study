# 문제 제약사향 최소 최대값
mx = -1000_000_000
mn = 1000_000_000

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

def dfs(idx, num):
    global mx, mn

    if idx == n-1:
        mx = max(mx, num)
        mn = min(mn, num)
        return

    new_idx = idx + 1
    if operators[0] != 0 : # 덧셈하는 경우
        operators[0] -= 1
        dfs(new_idx, num + numbers[new_idx])
        operators[0] += 1 

    if operators[1] != 0 : # 뺄셈하는 경우
        operators[1]-= 1
        dfs(new_idx, num - numbers[new_idx])
        operators[1] += 1
    
    if operators[2] != 0 : # 곱셈하는 경우
        operators[2] -= 1
        dfs(new_idx, num * numbers[new_idx])
        operators[2] += 1
    
    if operators[3] != 0 : #나눗셈하는 경우
        operators[3] -= 1
        dfs(new_idx, int(num/numbers[new_idx]))
        operators[3] += 1


dfs(0, numbers[0])
print(mx)
print(mn)