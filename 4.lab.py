import numpy as np
import matplotlib.pyplot as plt

with open('input.txt', 'r') as f:
    K = int(f.readline())
    A = np.array([list(map(int, line.split())) for line in f])

N = len(A)
print("Матрица A:\n", A)
F = A.copy()
print("Начальная F:\n", F)

n = N//2
E, B, D, C = A[:n,:n], A[:n,n:], A[n:,:n], A[n:,n:]
perim = np.r_[E[0,:], E[-1,:], E[1:-1,0], E[1:-1,-1]]
print(f"Сумма периметра E: {perim.sum()}, нулей: {(perim==0).sum()}")

if perim.sum() > (perim==0).sum():
    F[:n,n:], F[n:,n:] = C.T, B.T
    print("Поменяли B и C:\n", F)
else:
    F[:n,:n], F[:n,n:] = B, E
    print("Поменяли B и E:\n", F)

det_A, diag_F = np.linalg.det(A), F.trace()
print(f"Определитель A: {det_A}, сумма диагонали F: {diag_F}")

if det_A > diag_F:
    F = A @ A.T - K * F
else:
    F = (np.linalg.inv(A) + np.tril(A) - np.linalg.inv(F)) * K
print("Итоговая F:\n", F)

plt.figure(figsize=(6,4))
plt.imshow(F, cmap='coolwarm')
plt.colorbar()
plt.title("Тепловая карта F")
plt.show()

plt.figure(figsize=(6,4))
plt.bar(range(N), F.sum(axis=1), color='coral')
plt.title("Сумма строк F")
plt.xlabel("Строка")
plt.ylabel("Сумма")
plt.show()

plt.figure(figsize=(6,4))
plt.hist(F.flatten(), bins=10, color='lightblue', edgecolor='black')
plt.title("Гистограмма F")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.show()