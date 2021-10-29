

num = -432


def sum_of_digit(N):

    assert 0 <= N == int(N), "Number must be positive integer"
    if N == 0:
        return 0
    else:
        result = N % 10
        return result + sum_of_digit(N // 10)


print(sum_of_digit(num))




