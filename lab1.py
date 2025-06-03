import random


def print_matrix(matrix, title="Matrix"):
    print(f"{title}:")
    for row in matrix:
        print(" ".join(f"{elem:4}" for elem in row))
    print()


def input_matrix_from_file(filename, N):
    with open(filename, 'r') as file:
        matrix = []
        for _ in range(N):
            row = list(map(int, file.readline().split()))
            matrix.append(row)
        return matrix


def generate_random_matrix(N):
    return [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]


def is_symmetric(matrix):
    N = len(matrix)
    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def create_matrix_F(A):
    N = len(A)
    F = [row.copy() for row in A]

    if is_symmetric(A):
        for i in range(N // 2):
            for j in range(i + 1, N - i - 1):
                if j < N // 2:
                    F[i][j], F[N - 1 - j][N - 1 - i] = F[N - 1 - j][N - 1 - i], F[i][j]
    else:
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                F[i][j], F[i][N - 1 - j] = F[i][N - 1 - j], F[i][j]

    return F


def matrix_multiply(A, B):
    N = len(A)
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
    return result


def matrix_add(A, B):
    N = len(A)
    return [[A[i][j] + B[i][j] for j in range(N)] for i in range(N)]


def matrix_subtract(A, B):
    N = len(A)
    return [[A[i][j] - B[i][j] for j in range(N)] for i in range(N)]


def matrix_transpose(A):
    N = len(A)
    return [[A[j][i] for j in range(N)] for i in range(N)]


def matrix_scalar_multiply(K, matrix):
    N = len(matrix)
    return [[K * matrix[i][j] for j in range(N)] for i in range(N)]


def main():
    K = int(input("Введите K: "))
    N = int(input("Введите N: "))

    use_file = input("Использовать файл для ввода матрицы? (y/n): ").lower() == 'y'

    if use_file:
        filename = input("Введите имя файла: ")
        A = input_matrix_from_file(filename, N)
    else:
        A = generate_random_matrix(N)

    print_matrix(A, "Исходная матрица A")

    F = create_matrix_F(A)
    print_matrix(F, "Матрица F после преобразований")

    AT = matrix_transpose(A)
    print_matrix(AT, "Транспонированная матрица A^T")


    F_plus_A = matrix_add(F, A)
    print_matrix(F_plus_A, "F + A")

    K_F_plus_A = matrix_scalar_multiply(K, F_plus_A)
    print_matrix(K_F_plus_A, "K * (F + A)")

    K_F_plus_A_mult_AT = matrix_multiply(K_F_plus_A, AT)
    print_matrix(K_F_plus_A_mult_AT, "K * (F + A) * A^T")

    temp_result = matrix_subtract(K_F_plus_A_mult_AT, AT)
    print_matrix(temp_result, "K * (F + A) * A^T - A^T")

    final_result = matrix_add(temp_result, F)
    print_matrix(final_result, "Итоговая матрица (K * (F + A) * A^T - A^T + F)")


if __name__ == "__main__":
    main()