def tub_sonlarni_tartiblash(f):
    def wrapper(nums):
        sonlar = [num for num in nums if isinstance(num, int) and num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]
        sorted_sonlar = sorted(sonlar)
        print(f(sorted_sonlar))

    return wrapper


@tub_sonlarni_tartiblash
def lists(a):
    return a


A = ['a', 1, 2, 'sd', 11, 17, 21, 'fhjaf', 23, 25]
lists(A)
