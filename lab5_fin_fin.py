import time
import math

def F_recursive(n):
    if n < 2:
        return 3
    sign = -1 if n % 2 else 1
    fact_n = math.factorial(n)
    fact_2n = math.factorial(2 * n)
    return sign * (F_recursive(n - 1) / fact_n + F_recursive(n - 2) / fact_2n)

def F_iterative(n):
    if n < 2:
        return 3

    a0 = 3
    a1 = 3

    fact_i = 1
    fact_2i = 2

    for i in range(2, n + 1):
        sign = -1 if i % 2 else 1

        fact_i *= i
        fact_2i *= (2 * i - 1) * (2 * i)

        a2 = sign * (a1 / fact_i + a0 / fact_2i)
        a0, a1 = a1, a2

    return a1

def test_performance(max_n=10):
    print("n\tРекурсия (мс)\tИтерация (мс)\tРекур. знач.\tИтер. знач.")
    print("------------------------------------------------------------------")

    for n in range(0, max_n + 1):
        # Тест рекурсивной версии
        start = time.time()
        rec_val = F_recursive(n)
        recursive_time = (time.time() - start) * 1000

        # Тест итерационной версии
        start = time.time()
        iter_val = F_iterative(n)
        iterative_time = (time.time() - start) * 1000

        print(f"{n}\t{recursive_time:.4f}\t\t{iterative_time:.4f}\t\t{rec_val:.12f}\t{iter_val:.12f}")

print("Сравнительный анализ рекурсивного и итерационного подходов:")
test_performance()

print("\nПример вычисления для n=5:")
print(f"Рекурсивно: F(5) = {F_recursive(5)}")
print(f"Итерационно: F(5) = {F_iterative(5)}")