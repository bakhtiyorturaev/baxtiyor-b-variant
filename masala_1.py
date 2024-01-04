def faktorial_n_dan_m_gacha(n, m):
    result = 1
    for i in range(n, m + 1):
        result *= i
    count = 0
    while result % 10 == 0:
        count += 1
        result //= 10
    return count


n = int(input("n ni kiriting: "))
m = int(input("m ni kiriting: "))

nollar_soni = faktorial_n_dan_m_gacha(n, m)
print(f"{n} dan {m} gacha bo'lgan sonlar ko'paytmasidagi oxirida hosil bo'lgan nollar soni: {nollar_soni}")
