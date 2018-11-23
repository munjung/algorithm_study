# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

def solution(s):
    answer = ''
    list_s = list(s)
    list_s.sort(reverse = True)
    answer = ''.join(list_s)
    return answer


# String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요. 
# seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# Kim은 반드시 seoul 안에 포함되어 있습니다.

def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
    	if 'Kim' in seoul[i]:
    		answer = str(i)
    return '김서방은 '+answer+'에 있다'

solution(seoul)

