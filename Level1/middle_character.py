#단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 
#단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
#s는 길이가 1 이상, 100이하인 스트링입니다.

def solution(s):
    answer = ''
    quotient = len(s)//2
    remainder = len(s)%2

    if remainder == 0:
    	answer = s[quotient-1:quotient+1]
    else:
    	answer = s[quotient]

    return answer



# 함수 solution은 정수 x와 자연수 n을 입력 받아, 
# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.


def solution(x, n):
    answer = []
    for i in range(n):
    	answer.append(x*(i+1))
    return answer

