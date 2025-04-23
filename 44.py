import numpy as np
import matplotlib.pyplot as plt

def get_matrix(N):
    try:
        A = np.loadtxt("matrix_data.txt", dtype=int)
    except OSError:
        A = np.random.randint(-10, 11, (N, N))
    if np.linalg.det(A) == 0:
        raise ValueError("Определитель равен 0!")
    return A

def process_matrix(A):
    N, h, F = A.shape[0], A.shape[0]//2, A.copy()
    if N % 2 != 0:
        raise ValueError("N должен быть четным!")
    E, B, D, C = A[:h, :h], A[:h, h:], A[h:, :h], A[h:, h:]
    p = np.sum(C[0]) + np.sum(C[-1]) + np.sum(C[:, 0]) + np.sum(C[:, -1]) - C[0, 0] - C[0, -1] - C[-1, 0] - C[-1, -1]
    if np.count_nonzero(C[:, 1::2] == 0) > p:
        F[:h, h:], F[h:, h:] = F[h:, h:].copy(), F[:h, h:].copy()
    else:
        F[:h, :h], F[h:, h:] = F[h:, h:].copy(), F[:h, :h].copy()
    return F

def plot_graphs(F):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(F, cmap='coolwarm')
    plt.title("Тепловая карта F")
    plt.subplot(1, 3, 2)
    plt.plot(np.mean(F, axis=1), '-o')
    plt.title("Средние по строкам")
    plt.subplot(1, 3, 3)
    plt.hist(F.flatten(), bins=20, color='skyblue')
    plt.title("Гистограмма элементов")
    plt.tight_layout()
    plt.show()

def main():
    N, K = 4, int(input("Введите K: "))
    A = get_matrix(N)
    F, G = process_matrix(A), np.tril(A)
    det_A, det_F, det_G = np.linalg.det(A), np.linalg.det(F), np.linalg.det(G)
    inv_A, inv_F, inv_G = np.linalg.inv(A) if det_A != 0 else None, np.linalg.inv(F) if det_F != 0 else None, np.linalg.inv(G) if det_G != 0 else None
    if det_A > np.trace(F) + np.trace(np.fliplr(F)):
        result = inv_A @ A.T - K * F if inv_A is not None and inv_F is not None else "Ошибка"
    else:
        result = (inv_A + inv_G - inv_F) * K if inv_A is not None and inv_G is not None and inv_F is not None else "Ошибка"
    print("Матрица A:\n", A, "\nМатрица F:\n", F, "\nРезультат:\n", result)
    plot_graphs(F)

if __name__ == "__main__":
    main()