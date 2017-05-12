# -*- coding: utf-8 -*-
count = 0

# 1. while [조건식] - 조건식이 만족할 때 까지 반복한다.
#    조건식 = count 가 10보다 작을때 블럭 실행
while count < 10 :
    # 1.1. count 를 출력
    print("while count=" + str(count))
    # 1.2. count 가 0 에서 시작해서 반복할때마다 1씩 증가한다. 10번 반복하고 while문을 빠져나간다.
    count = count + 1

# 2. for 개별요소 in 요소들 - 특정 요소들의 범위내에서 개별요소 단위로 반복하고자 할 때 사용한다.
# 2.1. 문자열 선언
chars = "abcdefg"
# 2.2. 문자열 abcdefg 를 한문자씩 반복하면서 문자요소 하나하나를 꺼내서 c 변수에 담는다.
for c in chars :
    # 2.3. 문자 한개단위씩 출력
    print("for 1 :"+c)

# 3.1. 문자열로 된 리스트(일종의 배열) 선언
array = ["Hello ", "I ", "am ", "Python"]
# 3.2. 4개의 문자열을 가진 리스트를 반복하면서 문자열단위로 char 변수에 담는다
for char in array :
    # 3.3. char 문자열 단위로 출력
    print("for 2 :"+char)

# 4.1. 3.2와 동일
for chars in array :
    # 4.2 char 에 담은 문자열을 문자 하나씩 꺼내서 c 변수에 담는다
    for c in chars :
        # 4.3 문자 하나씩 출력
        print("for 3 :"+c)
