import time
import itertools
from functools import reduce

def algorithmic_assignments(K, N):
    def backtrack(used_fighters, current_assignment):
        if len(current_assignment) == min(K, N):
            result.append(current_assignment[:])
            return
        for fighter in range(K):
            if not used_fighters[fighter]:
                for obj in range(N):
                    if obj not in [assignment[1] for assignment in current_assignment]:
                        used_fighters[fighter] = True
                        current_assignment.append((fighter, obj))
                        backtrack(used_fighters, current_assignment)
                        current_assignment.pop()
                        used_fighters[fighter] = False
    result = []
    backtrack([False] * K, [])
    return result

def python_assignments(K, N):
    fighters = range(K)
    objects = range(N)
    if K >= N:
        return list(itertools.permutations(fighters, N))
    else:
        return list(itertools.combinations(objects, K))

def main_part1():
    K, N = 3, 3
    print(f"K = {K}, N = {N}")

    start_time = time.time()
    algo_result = algorithmic_assignments(K, N)
    algo_time = time.time() - start_time
    print(f"Алгоритмический метод: {len(algo_result)} вариантов, время: {algo_time:.6f} сек")
    print("Пример первых 5 вариантов:", algo_result[:5])

    start_time = time.time()
    py_result = python_assignments(K, N)
    py_time = time.time() - start_time
    print(f"Метод Python: {len(py_result)} вариантов, время: {py_time:.6f} сек")
    print("Пример первых 5 вариантов:", py_result[:5])

if __name__ == "__main__":
    main_part1()