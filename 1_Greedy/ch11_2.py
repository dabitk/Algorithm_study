# 0이 나오면 + 로 처리. 
# 0이 아닌 숫자는 전부 x로 처리. + 보다 더 많이 증가하는 연산자이기 때문.

# 문자열로 받는다
data = input()

result = int(data[0]) # 문자열 -> 숫자 형변환

for i in data[1:] : # [1:]인덱스 1 부터 시작하는 파이썬 문법
    current_number = int(i)
    if(current_number == 0 or result == 0): # OR 조건은 인풋이 0부터 시작하는 경우 예외케이스 처리용
        result += current_number
    else: 
        result *= current_number

print(result)