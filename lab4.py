import math

def next_permutation(perm):
    n = len(perm)
    # Знаходимо такі числа aj і aj+1, що (aj < aj+1)  (aj+1 > aj+2>…> an)
    j = n - 2
    while j >= 0 and perm[j] >= perm[j + 1]:
        j -= 1

    if j == -1:
        # Вхідна перестановка була останньою в лексикографічному порядку
        return None
    # Знаходимо найменше число з aj+1, aj+2, ..., an, яке більше за aj
    k = n - 1
    while perm[k] <= perm[j]:
        k -= 1
    # Міняємо місцями числа aj і ak
    perm[j], perm[k] = perm[k], perm[j]
    # Розвертаємо числа aj+1, aj+2, ..., an в висхідному порядку
    left = j + 1
    right = n - 1
    while left < right:
        perm[left], perm[right] = perm[right], perm[left]
        left += 1
        right -= 1
    # Повертаємо отриману перестановку
    return perm

# Ввід значення n
n = int(input("Введіть натуральне число n: "))

# Лексикографічно найменша перестановка 123...n
initial_permutation = list(range(1, n + 1))
print("Лексикографічно найменша перестановка:", initial_permutation)

# Обчислення n!
factorial = math.factorial(n)
# Побудова наступних перестановок
perm = initial_permutation
for i in range(1, factorial):
    perm = next_permutation(perm)
    print("Наступна перестановка:", perm)

print("----2-----")

def next_combination(comb, n, r):
    for i in range(r - 1, -1, -1):
        if comb[i] != n - r + i + 1:
            j = comb[i]
            while j in comb[:i]:
                j += 1
            comb[i] = j
            return comb

    return None

# Ввід значень n та r
n = int(input("Введіть натуральне число n: "))
r = int(input("Введіть невід'ємне ціле число r (r ≤ n): "))

# Лексикографічно найменше r-сполучення
initial_combination = list(range(1, r + 1))
print("Лексикографічно найменше сполучення:", initial_combination)

# Обчислення n!/(r!(n-r)!)
num_combinations = math.comb(n, r)

# Побудова наступних сполучень
comb = initial_combination
for i in range(1, num_combinations):
    comb = next_combination(comb, n, r)
    print("Наступне сполучення:", comb)
