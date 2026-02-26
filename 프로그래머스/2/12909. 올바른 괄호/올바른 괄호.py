def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    left = []
    
    for i in range(len(s)):
        if s[i] == "(":
            left.append(s[i])
        else:
            if not left:
                return False
            else:
                left.pop()
    
    if (len(left) == 0):
        return True
    else:
        return False
    
    return True