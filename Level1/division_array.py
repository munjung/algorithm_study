#array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
#divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
# arr은 자연수를 담은 배열입니다.
# 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다.
# array는 길이 1 이상인 배열입니다.


def solution(arr, divisor):
    answer = []
    count = 0
    for i in range(len(arr)):
    	if arr[i]%divisor == 0:
    		answer.append(arr[i])
    		count+=1
    if count == 0:
    	answer.append(-1)
    answer.sort()
    return answer


#정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

def solution(arr):
    answer = sum(arr)/len(arr)
    return answer

def solution(arr):
    answer = 0
    for i in range(len(arr)):
		answer += arr[i]
	return answer/len(arr)
