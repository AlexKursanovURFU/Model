import matplotlib.pyplot as plt
import numpy as np

def save_plot(filename, dpi=300, bbox_inches='tight'):
    """
    Сохраняет текущий график в файл.

    Параметры:
    ----------
    filename : str
        Путь и имя файла (например, 'graph.png').
    dpi : int, optional
        Качество сохранения (точек на дюйм). По умолчанию 300.
    bbox_inches : str, optional
        Контроль обрезки. По умолчанию 'tight' (без лишних полей).
    """
    plt.savefig(filename, dpi=dpi, bbox_inches=bbox_inches)
    print(f"График сохранён как {filename}")

def plot_graph(
    x_data,
    y_data=None,
    y_data_list=None,
    title="График",
    x_label="Ось X",
    y_label="Ось Y",
    colors=None,
    linestyles=None,
    linewidth=1,
    markers=None,
    labels=None,
    grid=True,
    show=True,
    figsize=(8,6)
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
    show : bool, optional
        Показывать график.
    """
    plt.figure(figsize=figsize)

    # Обработка нескольких графиков
    if y_data_list is not None:
        num_plots = len(y_data_list)
        
        # Установка значений по умолчанию
        colors = colors or plt.cm.tab10(np.linspace(0, 1, num_plots))
        linestyles = linestyles or ['-'] * num_plots
        markers = markers or [None] * num_plots
        labels = labels or [f'График {i+1}' for i in range(num_plots)]
        
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
        
        if labels:
            plt.legend()
    
    # Один график
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

    if show:
        plt.show()
    
    #plt.close()
