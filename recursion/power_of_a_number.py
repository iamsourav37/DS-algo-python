
base = 2
expo = 4


def power(base, expo):
    if expo == 0:
        return 0
    elif expo == 1:
        return base
    return base * power(base, expo-1)


print(power(base, expo))
print(pow(-2, 3))
