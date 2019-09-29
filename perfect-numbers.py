def get_factors(num):
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            yield i


m, n = input("m n: ").split()

for num in range(int(m), int(n) + 1):
    factors = get_factors(num)
    if sum(factors) == num:
        print(num, end=" ")
