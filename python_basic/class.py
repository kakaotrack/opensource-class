# -*- coding: utf-8 -*-
# 1. class 선언
class ClassName():
    # 1.2. 멤버변수
    member = 0
    # 1.3. 멤버함수
    #     * Python 만의 특징인데 첫번째 인자로 객체자신인 self를 받는다. 따라서 멤버변수는 self.멤버변수의 형태로 사용할 수 있다.
    def memberAdd(self, a) :
        self.member = self.member + a
    # 1.4. 멤버변수를 출력하는 함수
    def memberPrint(self) :
        print(self.member)

# 2. class 사용
clazz = ClassName()
# 2.2 멤버함수 사용
#    * 멤버함수를 사용할 때 첫번째 인자인 self는 입력하지 않는다.
clazz.memberAdd(5)
clazz.memberAdd(5)
clazz.memberAdd(5)
# 2.3 멤버함수를 통한 출력
clazz.memberPrint()
