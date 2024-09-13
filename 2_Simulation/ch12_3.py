def solution(s):
    answer = 987654321
    if len(s) != 1:
        for i in range(len(s) - 1): # 문자열 길이 - 1 만큼까지만 확인. (문자열 길이 만큼 압축한다는 것은 그냥 원문 그대로를 의미)
            answer = min(answer, len(get_zip_string(i+1, s)))
        return answer
    else: # s 길이가 1인 경우는 답은 그냥 1임
        return 1


def get_sublist_of_size_n(n, str_data):
    sublist = [str_data[i * n:(i + 1) * n] for i in range((len(str_data) + n - 1) // n )]
    # print(sublist)
    return sublist

def get_zip_string(n, str_data):
    sublist = get_sublist_of_size_n(n, str_data)
    zip_string = ''
    count = 1
    for i in range(1, len(sublist)): # 인덱스 1(두번째 원소) 부터 반복문 시작
        if sublist[i] == sublist[i - 1]:
            count += 1
            if i == len(sublist) - 1: # 리스트의 마지막 두개 원소가 동일하면서 현재 위치가 마지막 인덱스인 경우의 예외처리
                zip_string += (str(count) + sublist[i-1])
        else:
            # 앞축 문자열 부분 append 로직
            if count == 1 : # 반복 부분 문자열이 1개뿐인 경우 압축 결과에서 문자 앞의 1은 생략
                zip_string += sublist[i-1]
            else: # 반복 부분 문자열이 2개 이상인 경우는 반복 횟수를 문자 앞에 추가
                zip_string += (str(count) + sublist[i-1])
                
            count = 1 # 부분 문자열 반복 횟수 초기화
            
            if i == len(sublist) - 1:
                zip_string += sublist[i]
    # print(zip_string + str(len(zip_string)))
    return zip_string
    