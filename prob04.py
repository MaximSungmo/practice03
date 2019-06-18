# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.
import random

selection_no = 9
start_num = 1
last_num = 10

selection = {}
correction = {}
# 0부터 10미만 int 값을 랜덤으로 반환

def setquiz() :
    while len(selection) < selection_no:
        lv= random.randrange(start_num, last_num)
        rv= random.randrange(start_num, last_num)
        result = lv * rv
        value = '{0} * {1}'.format(lv, rv)
        selection.update({
            result : value
        })
    else:
        # selection 확인용
        # print(selection)
        a = list(selection.keys())
        a =  a[random.randrange(start_num, last_num)-1]
    return a

a = setquiz()

while(True):
    # 보기 출력용
    counter = int(selection_no**0.5)
    index = 1
    for s in selection:
        if index%counter == 0:
            print(s, end='\n')
        else:
            print(s, end='\t')
        index += 1

    # 문제 묻기
    print(selection.get(a))

    num = int(input('정답을 입력하세요 >>'))

    # 정답 확인용
    # print(a)

    if int(a) == num:
        print('정답입니다.')
        break
    else:
        print('오답입니다.')
        continue
