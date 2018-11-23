#배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
#예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, 
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
    	_arr = array[commands[i][0]-1:commands[i][1]]
    	_arr.sort()
    	answer.append(_arr[commands[i][2]-1])
    return answer


# 문자열 s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수, solution을 완성하세요.
# 예를들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

def solution(s):
    answer = False
    if s.isdigit():
    	if len(s) == 4 or len(s) == 6:
    		answer = True
    return answer
