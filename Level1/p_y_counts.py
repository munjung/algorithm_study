# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
#s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
#'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
# 예를들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.
# 제한사항
# 문자열 s의 길이 : 50 이하의 자연수
# 문자열 s는 알파벳으로만 이루어져 있습니다.


def solution(s):
    answer = False
    s = s.lower()
    p_count = 0
    y_count = 0

    #if s.find('p') == -1 and s.find('y') == -1:
    if 'p' not in s and 'y' not in s:
    	answer = True
	   	
    if answer == False:
    	for i in range(len(s)):
    		if 'p' in s[i]:
    			p_count += 1
    		if 'y' in s[i]:
    			y_count += 1

    if p_count == y_count:
    	answer = True

    return answer

# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

def solution(n):
    list_n = [int(x) for x in str(n)]
    answer = sum(list_n[0:len(list_n)])
    return answer
