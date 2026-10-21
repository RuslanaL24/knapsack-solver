"""
Knapsack Problem Solver
Решает задачу о рюкзаке методом динамического программирования.
Возвращает максимальную ценность и список выбранных предметов.
"""

def solve_knapsack(weights, values, capacity):
    """
    weights: список весов предметов
    values: список ценностей предметов
    capacity: максимальная грузоподъёмность
    """
    n = len(weights)
    # dp[i][w] = максимальная ценность, используя первые i предметов при вместимости w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Восстановление выбранных предметов
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]
    selected.reverse()

    return dp[n][capacity], selected


if __name__ == "__main__":
    # Пример: предметы (вес, ценность)
    items = [
        ("Ноутбук", 3, 1000),
        ("Камера", 1, 500),
        ("Телефон", 2, 700),
        ("Часы", 1, 200),
    ]
    weights = [item[1] for item in items]
    values = [item[2] for item in items]
    capacity = 4

    max_value, chosen_indices = solve_knapsack(weights, values, capacity)

    print(f"Максимальная ценность: {max_value}")
    print("Выбранные предметы:")
    for idx in chosen_indices:
        name, w, v = items[idx]
        print(f"  - {name} (вес: {w}, ценность: {v})")
