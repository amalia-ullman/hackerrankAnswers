def iterfactorial(x):
    answer = 1
    for i in range(1, x+1):
        answer = answer * i
    return answer

print(iterfactorial(4))


def recursivefactorial(y):
    if y == 0:
        return 1
    else:
        return y * recursivefactorial(y-1)

print(recursivefactorial(4))