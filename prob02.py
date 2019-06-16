# range() 함수와 유사한 frange() 함수를 작성해 보세요. frange() 함수는 실수 리스트를 반환합니다.
from decimal import Decimal

print(range(10))

def frange(end, start=0.0, step=0.1):
    results = []
    while(start < end):

        results.append(start)
        # start = fsum([step, start])
        start = Decimal(start)+Decimal(step)
    return results


print(frange(1.0, 0.0, 0.1))

print(Decimal(0.2)+Decimal(0.1))