# -*- coding: utf-8 -*-
var_a = 145
var_b = 13

# 1. 함수의 선언
def sumNumbers(a,b) : # 2. 블럭의 시작은 : (콜론)
    return a + b
# 3. 블럭의 구분은 들여쓰기

# 4. 들여쓰기가 끝나면 새로운 블럭이 시작된다
def multiNumbers(a,b) :
    return a * b

def complex(a,b) :
# --- complex 함수 블럭 시작
    com_a = sumNumbers(a,b)
    com_b = multiNumbers(a,b)
    # 5. 함수 내에서 if 문과 같은 새로운 블럭이 필요할 때에도 : 으로 시작하고 들여쓰기를 해야한다.
    if com_a > com_b :
        return com_a
    else :
        return com_b
# --- complex 함수 블럭 종료

# 7. 결과 확인
print(sumNumbers(var_a,var_b))   # 결과 : 158
print(multiNumbers(var_a,var_b)) # 결과 : 1885

print(complex(5,7))  # 결과 : 35
print(complex(5,-7)) # 결과 : -2
