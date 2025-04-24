import matplotlib.pyplot as plt
import numpy as np

def plot_graph_1(
    x_data,
    y_data=None,
    y_data_list=None,  # Список наборов данных для Y
    title="График",
    x_label="Ось X",
    y_label="Ось Y",
    figsize=(8,6),      # Размер фигуры
    colors=None,       # Список цветов (по умолчанию автоматический подбор)
    linestyles=None,    # Список стилей линий
    linewidth=1,
    markers=None,       # Список маркеров
    labels=None,        # Подписи для легенды
    grid=True,
    save_path=None,
    show=True,
):
    """
    Рисует один или несколько графиков.

    Параметры:
    ----------
    x_data : array-like
        Данные для оси X (общие для всех графиков).
    y_data : array-like, optional
        Данные для оси Y (если один график).
    y_data_list : list of array-like, optional
        Список данных для оси Y (если несколько графиков).
    title : str, optional
        Заголовок графика.
    x_label, y_label : str, optional
        Подписи осей.
    colors : list of str, optional
        Список цветов для линий.
    linestyles : list of str, optional
        Список стилей линий (например, '-', '--', ':').
    linewidth : int or list of int, optional
        Толщина линий.
    markers : list of str, optional
        Список маркеров (например, 'o', 's', '^').
    labels : list of str, optional
        Подписи для легенды.
    grid : bool, optional
        Отображать сетку.
    save_path : str, optional
        Путь для сохранения графика.
    show : bool, optional
        Показывать график.
    """
    plt.figure(figsize=figsize)

    # Если передан y_data_list, рисуем несколько графиков
    if y_data_list is not None:
        num_plots = len(y_data_list)
        
        # Устанавливаем значения по умолчанию, если не переданы
        if colors is None:
            colors = plt.cm.tab10(np.linspace(0, 1, num_plots))  # Автоподбор цветов
        if linestyles is None:
            linestyles = ['-'] * num_plots
        if markers is None:
            markers = [None] * num_plots
        if labels is None:
            labels = [f'График {i+1}' for i in range(num_plots)]
        
        # Рисуем все графики
        for i in range(num_plots):
            plt.plot(
                x_data,
                y_data_list[i],
                color=colors[i],
                linestyle=linestyles[i],
                linewidth=linewidth,
                marker=markers[i],
                label=labels[i],
            )
        
        # Добавляем легенду, если есть подписи
        if labels is not None:
            plt.legend()
    
    # Иначе рисуем один график (если передан y_data)
    elif y_data is not None:
        plt.plot(
            x_data,
            y_data,
            color=colors[0] if colors else 'blue',
            linestyle=linestyles[0] if linestyles else '-',
            linewidth=linewidth,
            marker=markers[0] if markers else None,
            label=labels[0] if labels else None,
        )
        if labels:
            plt.legend()
    else:
        raise ValueError("Необходимо передать y_data или y_data_list")

    # Общие настройки
    plt.title(title, fontsize=14)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.grid(grid)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    if show:
        plt.show()
    
    plt.close()

# Пример использования
if __name__ == "__main__":
    x = np.linspace(0, 10, 100)
    
    
    plot_graph_1(
        x_data=x,
        y_data_list=[np.sin(x), np.cos(x), np.sin(x) + 0.5 * np.cos(2 * x)],
        title="Сравнение функций",
        x_label="x",
        y_label="y",
        figsize=(10,8),
        colors=["red", "green", "blue"],
        linestyles=["-", "--", ":"],
        markers=[None, "o", None],
        labels=["sin(x)", "cos(x)", "sin(x) + 0.5cos(2x)"],
        linewidth=2,
        save_path="multi_plot.png",
    )