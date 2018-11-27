#오늘은 체육수업이 있는 날입니다. 그런데 점심시간에 도둑이 들어 몇몇 학생의 체육복이 도난을 당했습니다. 
#다행히 일부 학생들이 여벌의 체육복을 가져왔습니다. 
#학생들의 번호는 체격 순으로 매겨져 있기 때문에 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려주려고 합니다.

# 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
# 당연히 체육복을 2벌 가져온 학생의 체육복이 도난을 당했다면, 여벌의 체육복을 빌려줄 수 없습니다.

# 체육복이 없으면 체육수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 듣고 싶습니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

def solution(n, lost, reserve):
    result = []
    lost_sort = list(set(lost) - (set(lost) & set(reserve)))
    reserve_sort = list(set(reserve) - (set(lost) & set(reserve)))
    lost_sort.sort()
    reserve_sort.sort()
    for i in range(len(lost_sort)):
        if len(reserve_sort) == 0:
            break
        for j in range(len(reserve_sort)):
            if abs(lost_sort[i]-reserve_sort[j]) <= 1:
                result.append(lost_sort[i])
                reserve_sort.pop(j)
                break
    answer = n-len(lost_sort)+len(result)   
    return answer
