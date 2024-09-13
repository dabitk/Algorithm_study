# 문자열로 받는다
data = input()
firstpart, secondpart = data[:len(data)//2], data[len(data)//2:] # 문자열을 중간에서 잘라서 두개의 부분 문자열 생성

def list_sum(number_string):

    int_list = [int(number_char) for number_char in number_string] # 문자열 -> 각 자릿수 문자를 숫자 리스트로 변환
    return sum(int_list) # 숫자 리스트의 모든 원소의 합을 리턴



if list_sum(firstpart) == list_sum(secondpart):
    print("LUCKY")
else:
    print("READY")