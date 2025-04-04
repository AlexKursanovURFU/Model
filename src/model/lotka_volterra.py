def lotka_volterra(t, y, a=1.1, b=0.4, c=0.1, d=0.4):
    """
    Система уравнений Лотки-Вольтерры для динамики популяций хищников и жертв.

    Args:
        t (float): Время (не используется, но требуется для solve_ivp).
        y (list): Текущие значения [жертвы, хищники].
        a, b, c, d (float): Параметры модели.

    Returns:
        list: Производные [dy1/dt, dy2/dt].

    Пример:
        >>> lotka_volterra(0, [10, 5])
        [6.0, 1.5]
    """
    return [
        a * y[0] - b * y[0] * y[1],
        -c * y[1] + d * y[0] * y[1]
    ]