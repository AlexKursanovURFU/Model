from logger_config import setup_logger
from scipy_solver import ScipySolver
import model as comp_model
import matplotlib.pyplot as plt
import numpy as np
from Plot_graph_1 import plot_graph_1
from plot_graph_plot_save import plot_graph
from plot_graph_plot_save import save_plot


def exp_1(t_span, number_macrofags, g_gap = 0.1):
    # Настройка логирования
    logger = setup_logger(log_file = "logs/solver.log")
    
    try:
        logger.info("Запуск прокотола 1...")


        logger.info("Инициализация констант и начальных значений...")
        init_states, constants = comp_model.initConsts()

        V = {}
        time = {}
        V_macro = {}

        for number_macrofag in number_macrofags:

            logger.info(f"Расчет модели с числом макрофагов {number_macrofag}")

            constants[58] = number_macrofag
            constants[59] = g_gap
            
            solver = ScipySolver(
                logger = logger,    
                model=comp_model.computeRates,
                t_span=t_span,
                y0=init_states,
                args=constants)
            
            voi, states = solver.solve()

            V[number_macrofag] = states[0,:]
            time[number_macrofag] = voi
            V_macro[number_macrofag] = states[29,:]



        for number_macrofag in number_macrofags:
            #plt.plot(time[number_macrofag],V[number_macrofag], label = f'Число макрофагов: {number_macrofag}')
            plot_graph(
                x_data=time[number_macrofag],
                y_data_list=[V[number_macrofag]],
                title="____",
                x_label="x", 
                y_label="y",
                colors=[None],
                linestyles=[None],
                markers=[None, "o", None],
                labels=[f'Число макрофагов: {number_macrofag}'],
                linewidth=2,
                show=False,
                figsize=(10,8)
            )
        save_plot("plot4.png")
        plt.close()
        # Расчет до 10 с.
        # Поварьировать g_gap = [0.1, 0.5, 1]

        # График (число макрофагов, частота стимуляции)
        # График (число макрофагов, максимум ПД)
        # График (число макрофагов, минимум ПД)
        # График (число макрофагов, амрлитула ПД)
        # График (число макрофагов, длительность потенциала действия)
        

        logger.info("Программа завершена успешна")

    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)