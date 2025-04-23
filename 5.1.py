import time
import itertools
import random

def algorithmic_assignments_with_constraints(K, N, fighter_levels, object_difficulties):
    def backtrack(used_fighters, current_assignment):
        if len(current_assignment) == min(K, N):
            result.append(current_assignment[:])
            return
        for fighter in range(K):
            if not used_fighters[fighter]:
                for obj in range(N):
                    if obj not in [assignment[1] for assignment in current_assignment] and fighter_levels[fighter] >= object_difficulties[obj]:
                        used_fighters[fighter] = True
                        current_assignment.append((fighter, obj))
                        backtrack(used_fighters, current_assignment)
                        current_assignment.pop()
                        used_fighters[fighter] = False
    result = []
    backtrack([False] * K, [])
    return result

def python_assignments_with_constraints(K, N, fighter_levels, object_difficulties):
    fighters, objects = range(K), range(N)
    if K >= N:
        perms = itertools.permutations(fighters, N)
        return [list(zip(perm, range(N))) for perm in perms if all(fighter_levels[f] >= object_difficulties[obj] for f, obj in zip(perm, range(N)))]
    else:
        combs = itertools.combinations(objects, K)
        return [list(zip(range(K), comb)) for comb in combs if all(fighter_levels[f] >= object_difficulties[obj] for f, obj in zip(range(K), comb))]

def optimize_assignments(assignments, fighter_levels):
    if not assignments:
        return None, 0
    best_assignment = max(assignments, key=lambda assignment: sum(fighter_levels[fighter] for fighter, _ in assignment))
    return best_assignment, sum(fighter_levels[fighter] for fighter, _ in best_assignment)

def main_part2():
    K, N = 3, 3
    random.seed(42)
    fighter_levels = [random.randint(1, 10) for _ in range(K)]
    object_difficulties = [random.randint(1, 10) for _ in range(N)]
    print(f"K = {K}, N = {N}")
    print(f"Уровни бойцов: {fighter_levels}")
    print(f"Сложности объектов: {object_difficulties}")

    start_time = time.time()
    algo_result = algorithmic_assignments_with_constraints(K, N, fighter_levels, object_difficulties)
    algo_time = time.time() - start_time
    algo_best, algo_score = optimize_assignments(algo_result, fighter_levels)
    print(f"Алгоритмический метод: {len(algo_result)} вариантов, время: {algo_time:.6f} сек")
    print(f"Лучшее назначение: {algo_best}, сумма уровней: {algo_score}")

    start_time = time.time()
    py_result = python_assignments_with_constraints(K, N, fighter_levels, object_difficulties)
    py_time = time.time() - start_time
    py_best, py_score = optimize_assignments(py_result, fighter_levels)
    print(f"Метод Python: {len(py_result)} вариантов, время: {py_time:.6f} сек")
    print(f"Лучшее назначение: {py_best}, сумма уровней: {py_score}")

if __name__ == "__main__":
    main_part2()