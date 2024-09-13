# 문자열로 받는다
data = input()

sum = 0
list = []
result = ''

for char_data in data:
    if char_data.isalpha():
       list.append(char_data) # 문자는 별도 리스트로 보관
    else: # 알파벳이 아니면 숫자임
        sum += int(char_data) # 숫자는 누적합 계산해서 변수에 저장

list.sort() # 리스트 오름차순 정렬

for element in list:
    result += element # 문자 리스트 -> 문자열로 이어붙이기
result += str(sum) # 맨 마지막에 누적합 구해둔 숫자 이어붙이기

print(result) # 결과 출력