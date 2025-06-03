import numpy as np
import matplotlib.pyplot as plt


def input_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    matrix = []
    for line in lines:
        row = list(map(int, line.strip().split()))
        matrix.append(row)
    return np.array(matrix)


def generate_matrix(N):
    return np.random.randint(-10, 11, size=(N, N))


def print_matrix(matrix, name):
    print(f"Матрица {name}:")
    print(matrix)


def split_matrix(A):
    N = A.shape[0]
    half = N // 2
    B = A[:half, :half]
    C = A[:half, half:]
    D = A[half:, :half]
    E = A[half:, half:]
    return B, C, D, E


def form_matrix_F(A):
    N = A.shape[0]
    F = A.copy()
    B, C, D, E = split_matrix(A)

    zero_odd_cols_E = np.sum(E[:, ::2] == 0)

    negative_even_rows_E = np.sum(E[1::2, :] < 0)

    if zero_odd_cols_E > negative_even_rows_E:
        F[:N // 2, :N // 2], F[:N // 2, N // 2:] = C[:, ::-1], B[:, ::-1]
    else:
        F[:N // 2, :N // 2], F[N // 2:, N // 2:] = E, B

    return F


def compute_expression(A, F, K):
    det_A = np.linalg.det(A)
    sum_diag_F = np.trace(F) + np.trace(np.fliplr(F))

    if det_A > sum_diag_F:
        A_inv = np.linalg.inv(A)
        A_T = A.T
        result = np.dot(A_inv, A_T) - K * F
    else:
        G = np.tril(A)
        F_inv = np.linalg.inv(F)
        result = (A.T + G - F_inv) * K

    return result


def plot_matrix(matrix, title):
    plt.figure()
    plt.imshow(matrix, cmap='viridis')
    plt.colorbar()
    plt.title(title)
    plt.show()


def plot_histogram(matrix, title):
    plt.figure()
    plt.hist(matrix.flatten(), bins=20, color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel('Значение элемента')
    plt.ylabel('Частота')
    plt.show()


def plot_surface(matrix, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.meshgrid(np.arange(matrix.shape[1]), np.arange(matrix.shape[0]))
    ax.plot_surface(x, y, matrix, cmap='viridis')
    plt.title(title)
    plt.show()


def main():
    K = int(input("Введите K: "))
    N = int(input("Введите N (четное число): "))

    A = generate_matrix(N)
    print_matrix(A, "A")

    F = form_matrix_F(A)
    print_matrix(F, "F")

    result = compute_expression(A, F, K)
    print_matrix(result, "Результат вычисления выражения")

    plot_matrix(F, "Визуализация матрицы F")
    plot_histogram(F, "Гистограмма элементов матрицы F")
    plot_surface(F, "3D поверхность матрицы F")


if __name__ == "__main__":
    main()