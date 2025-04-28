import time
import matplotlib.pyplot as plt

def F_recursive(n):
    if n == 1 or n == 2: return 1
    return (-1)**n * (F_recursive(n-1) / n)

def F_iterative(n):
    if n == 1 or n == 2: return 1
    result = 1
    for i in range(3, n+1):
        result = (-1)**i * (result / i)
    return result

def measure_time(func, n):
    start = time.time()
    result = func(n)
    return result, time.time() - start

n_values = list(range(3, 1001, 100))
rec_times, iter_times, table = [], [], []

for n in n_values:
    rec_res, rec_t = measure_time(F_recursive, n)
    iter_res, iter_t = measure_time(F_iterative, n)
    rec_times.append(rec_t)
    iter_times.append(iter_t)
    table.append((n, rec_res, rec_t, iter_res, iter_t))
    print(f"n={n}: Rec={rec_res:.6f}, {rec_t:.6f}s; Iter={iter_res:.6f}, {iter_t:.6f}s")

print("\nТаблица:")
print("n\tRec(рез)\tRec(время)\tIter(рез)\tIter(время)")
for r in table:
    print(f"{r[0]}\t{r[1]:.6f}\t{r[2]:.6f}\t\t{r[3]:.6f}\t\t{r[4]:.6f}")

print("\nРекурсия неэффективна для n>500 из-за стека. Итерация быстрее.")

plt.plot(n_values, rec_times, 'o-', label="Рекурсия")
plt.plot(n_values, iter_times, 'x-', label="Итерация")
plt.xlabel("n"); plt.ylabel("Время (с)"); plt.title("Сравнение времени")
plt.legend(); plt.grid(True); plt.show()
