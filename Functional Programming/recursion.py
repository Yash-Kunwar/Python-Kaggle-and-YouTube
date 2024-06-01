def fact(n):
    factorial = 1
    for n in range(1, n+1):
        factorial = factorial*n
    return factorial


num = int(input('enter a no.: '))
print(fact(num))


def fact_recur(no):
    if no == 1 or no == 0:
        return 1
    return no*fact_recur(no-1)


print(fact_recur(10))
