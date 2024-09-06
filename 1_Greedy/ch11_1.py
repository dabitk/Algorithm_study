# N
n= map(int, input())
# 모험가 별 공포도
data = list(map(int, input().split()))

data.sort(reverse=True) # 입력받은 수들 "내림차순" 정렬하기

result = 0
data_size = len(data)

idx = 0
adventurer_fearness = 0

# 리스트를 수정하지 않고 인덱스만으로 접근해서 범위를 벗어나면 거기서 스톱함. 그룹을 형성하지 못한 '나머지' 그룹은 마을에 남는 그룹.
while True:
    if(idx >= data_size): # 인덱스가 리스트 범위를 벗어나면 루프 탈출
        break
    else:
        adventurer_fearness = data[idx] # 모험가 공포도


    idx += adventurer_fearness
    result += 1

print(result)