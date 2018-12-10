# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다.
# z는 1만큼 밀면 a가 됩니다.
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.

def solution(s, n):
    answer = []
    list_s = list(s)
    for i in range(len(list_s)):
        s_ord = ord(list_s[i])+n
        if ord(list_s[i]) == 32:
            answer.append(list_s[i])
            continue
        if list_s[i].islower():
            answer.append(chr(s_ord - 26)) if s_ord > 122 else answer.append(chr(s_ord))
        else:
            answer.append(chr(s_ord - 26)) if s_ord > 90 else answer.append(chr(s_ord))
    return ''.join(answer)
