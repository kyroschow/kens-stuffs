numbers = [int(x) for x in input("Enter numbers: ").split()]
size = len(numbers)

# Find all divisors of each number
maxNum = max(numbers)
allDivisors = []
for num in numbers:
    for divisor in [2] + list(range(3, int(maxNum / 2) + 1, 2)):
        if num % divisor == 0:
            allDivisors.append(divisor)
print(allDivisors)

# compare repeated divisors
# if no repeated divisors -> prp
# if occurrences are equal to length of numbers list
# then all the numbers are divisible by some number > 1 -> ~
# otherwise the numbers are mrp
uniqueDivisors = list(dict.fromkeys(allDivisors))
if len(uniqueDivisors) == len(allDivisors):
    print("prp")
    exit(0)
else:
    for uniqueDivisor in uniqueDivisors:
        divisorRepeat = 0
        for divisor in allDivisors:
            if divisor == uniqueDivisor:
                divisorRepeat += 1
        if divisorRepeat == size:
            print("~")
            exit(0)

print("mrp")
