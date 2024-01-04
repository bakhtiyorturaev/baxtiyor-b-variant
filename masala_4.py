def dec_func(origin_func):
    def wrapper(*args, **kwargs):
        val = origin_func(*args, **kwargs)
        for i in val:
            a = []
            for j in i:
                if i % j == 0:
                    a += 1
                    if a == 2:
                        a.append(i)
                        print(a)

    return wrapper


@dec_func
def lists(a):
    return a


A = ['a', 1, 2, 'sd',11]
lists(A)
