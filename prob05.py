# 문제5.
# 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.
#
#
# 문제 힌트 및 제한 :
#
# 선택 정렬은 다음과 같습니다.
# 정렬이 되지 않은 배열에서 최소값을 가장 뒤로 이동 시키는 방식으로 정렬시킵니다.
#
# 예를 들어,
#
# 초기값
# [ 5, 9, 3, 8, 60, 20, 1 ]
#
# 1회
# [ 9, 5, 3, 8, 60, 20, 1 ]  ->  5, 9를 비교해서 뒤가 크므로 바꾼다
# [ 9, 5, 3, 8, 60, 20, 1 ]  ->  5, 3을 비교해서 뒤가 작으므로 제자리
# [ 9, 5, 8, 3, 60, 20, 1 ]  ->  3, 8를 비교해서 뒤가 크므로 바꾼다
# [ 9, 5, 8, 60, 3, 20, 1 ]  ->  3, 60을 비교해서 뒤가 크므로 바꾼다
# [ 9, 5, 8, 60, 20, 3, 1 ]  ->  3, 20을 비교해서 뒤가 크므로 바꾼다
# [ 9, 5, 8, 60, 20, 3, 1 ]  ->  3, 1을 비교해서 뒤가 작으므로 제자리
#
# 2회 : 같은 방식
# [ 9, 8, 5, 60, 20, 3, 1 ]
# [ 9, 8, 60, 5, 20, 3, 1 ]
# [ 9, 8, 60, 5, 20, 3, 1 ]
# [ 9, 8, 60, 20, 5, 3, 1 ]
#
# 3회 : 같은 방식, 마지막 결과
# [ 9, 60, 20, 8, 5, 3, 1 ]
#
# 4회 : 같은 방식, 마지막 결과
# [ 60, 20, 9, 8, 5, 3, 1 ]
#


list_ = [5, 9, 3, 8, 60, 20, 1]

# 중복 탐색이 되지 않도록 해야함
for i in range(len(list_)):
    a = 0
    b = 1
    for j in range(i+1, len(list_)):
        if list_[a] < list_[b]:
            temp = list_[a]
            list_[a] = list_[b]
            list_[b] = temp
            # print(list_[a])
        else:
            print('-')
        print(i+1,'-',j, '회차', '\n', list_)
        a += 1
        b += 1

# for index_i, i in enumerate(list_):
#     for index_j, j in enumerate(list_):
#         if i < j:
#             temp = i
#             i = j
#             j = temp
#         else:
#             print('-')
#         print(index_i+1, '-', index_j, '회차', '\n', list_)







