# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
# 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
# 배열 arr에서 제거 되고 남은 수들을 return 하는 solution 함수를 완성해 주세요. 
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.
# 예를들면
# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

def solution(arr):
    answer = []
    for i in range(len(arr)):
		if i == 0:
			answer.append(arr[i])
		else:
			if arr[i-1] == arr[i]:
				pass
			else:
				answer.append(arr[i])
	return answer



# 자연수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
def solution(n):
    answer = 0
    for i in range(n, 0, -1):
        if n % i == 0:
            answer += i
    return answer
