

def factorial(num):
    if num < 0 or int(num) != num:
        raise Exception("Number must be a positive integer only")

    def get_fact(n):
        if n in [0, 1]:
            return 1
        else:
            return n * get_fact(n-1)
    return get_fact(num)


try:
    print(factorial(9))
except Exception as e:
    print(e)
