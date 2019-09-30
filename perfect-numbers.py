def get_factors(num):
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            yield i


def get_perfect_numbers(m, n):
    for num in range(m, n + 1):
        factors = get_factors(num)
        if sum(factors) == num:
            yield num


m, n = input("m n: ").split()
perfectNumbers = get_perfect_numbers(int(m), int(n))
print(*perfectNumbers)
