import time
from itertools import permutations


def algorithmic_approach(candidates):
    """Алгоритмический подход с вложенными циклами."""
    n = len(candidates)
    total = 0
    start_time = time.perf_counter()
    for i in range(n):  # PJ1
        for j in range(n):  # PJ2
            if j == i:
                continue
            for k in range(n):  # SR1
                if k == i or k == j:
                    continue
                for l in range(n):  # SR2
                    if l == i or l == j or l == k:
                        continue
                    total += 1

    end_time = time.perf_counter()
    print(f"[Алгоритмический] Вариантов: {total}, время: {(end_time - start_time) * 1000:.3f} мс")


def python_function_approach(candidates):
    start_time = time.perf_counter()
    total = len(list(permutations(candidates, 4)))
    end_time = time.perf_counter()
    print(f"[Функциональный] Вариантов: {total}, время: {(end_time - start_time) * 1000:.3f} мс")


def optimized_approach(candidates, experience):
    """Оптимизированный подход с ограничениями."""
    forbidden = {'A': ['SR1', 'SR2']}
    max_exp = -1
    best = None
    total_valid = 0
    start_time = time.perf_counter()

    for pj1, pj2, sr1, sr2 in permutations(candidates, 4):
        if pj1 == pj2 or sr1 == sr2:
            continue
        if 'A' in (sr1, sr2):
            continue
        total_valid += 1
        avg_exp = (experience[sr1] + experience[sr2]) / 2
        if avg_exp > max_exp:
            max_exp = avg_exp
            best = (pj1, pj2, sr1, sr2)

    end_time = time.perf_counter()
    print(f"[Оптимизированный] Валидных вариантов: {total_valid}, время: {(end_time - start_time) * 1000:.3f} мс")
    print(f"Лучшее распределение: PJ1={best[0]}, PJ2={best[1]}, SR1={best[2]}, SR2={best[3]}")
    print(f"Максимальный средний опыт SR: {max_exp}")


candidates = ['A', 'B', 'C', 'D']
experience = {'A': 1, 'B': 3, 'C': 5, 'D': 4}

print("=== Часть 1: Все варианты ===")
algorithmic_approach(candidates)
python_function_approach(candidates)

print("\n=== Часть 2: Оптимизированный вариант ===")
optimized_approach(candidates, experience)