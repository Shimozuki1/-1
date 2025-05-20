import time


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def F_recursive(n):
    if n < 2:
        return 3
    sign = -1 if n % 2 else 1
    fact_n = factorial_recursive(n)
    fact_2n = factorial_recursive(2 * n)
    return sign * (F_recursive(n - 1) / fact_n + F_recursive(n - 2) / fact_2n)


def F_iterative(n):
    if n < 2:
        return 3

    memo = [0] * (n + 1)
    memo[0], memo[1] = 3, 3

    facts = [1] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        facts[i] = facts[i - 1] * i

    for i in range(2, n + 1):
        sign = -1 if i % 2 else 1
        term1 = memo[i - 1] / facts[i]
        term2 = memo[i - 2] / facts[2 * i]
        memo[i] = sign * (term1 + term2)

    return memo[n]

def test_performance(max_n=20):
    print("n\tРекурсия (мс)\tИтерация (мс)\tРекур. знач.\tИтер. знач.")
    print("------------------------------------------------------------------")

    for n in range(1, max_n + 1):
        # Тест рекурсивной версии
        start = time.time()
        rec_val = F_recursive(n)
        recursive_time = (time.time() - start) * 1000

        # Тест итерационной версии
        start = time.time()
        iter_val = F_iterative(n)
        iterative_time = (time.time() - start) * 1000

        print(f"{n}\t{recursive_time:.4f}\t\t{iterative_time:.4f}\t\t{rec_val:.6f}\t{iter_val:.6f}")


if __name__ == "__main__":
    print("Сравнительный анализ рекурсивного и итерационного подходов:")
    test_performance()

    print("\nПример вычисления для n=5:")
    print(f"Рекурсивно: F(5) = {F_recursive(5)}")
    print(f"Итерационно: F(5) = {F_iterative(5)}")