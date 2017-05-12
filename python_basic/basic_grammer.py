# -*- coding: utf-8 -*-
#1. Python 은 변수의 타입이 없다
hong = 111

# 2. 문자변수의 입력은 쌍따옴표 또는 외따옴표를 앞뒤로 사용한다
words = "I am Python"

# 3. 동일한 변수명에 다른타입의 값을 입력할 수 있다.
words = 157 # 문자열 "I am Python" 를 입력했다가 다시 같은 변수에 숫자 157 입력

# 4. 문장의 끝은 줄바꿈으로 처리한다.
var_a = 145
var_b = "Hello"
var_c = "123"

# 5. 기본형에 대한 자동 형변환은 지원하지 않는다
result_char = str(var_a) + var_b # 숫자 var_a 를 문자열로 변경한 후  문자열 var_b와 더해준다.
result_num = var_a + int(var_c) # 문자열 "123" 을 숫자 123 으로 변경

# 6. 결과값 출력
print(result_char) # 결과 : 145Hello
print(result_num)  # 결과 : 268

# 7. 문자열 곱하기 (곱한숫자만큼 문자열을 반복해서 더한다음 리턴해준다)
print(var_b * 3) # 결과 : HelloHelloHello

# 8. 거듭제곱
print(var_a ** 3) # 결과 : 3048625 = 145 * 145 * 145
