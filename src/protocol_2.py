# Расчет до 10 с.
# Поварьировать g_gap = [0.1, 0.5, 1, 3]
# Поварьировать number_macrofag = [1, 2, 3]
# График (число g_gap, частота стимуляции)
# График (число g_gap, максимум ПД)
# График (число g_gap, минимум ПД)
# График (число g_gap, амрлитула ПД)
# График (число g_gap, длительность потенциала действия)


from logger_config import setup_logger
from scipy_solver import ScipySolver
import model as comp_model
import matplotlib.pyplot as plt
import numpy as np

def protocol_2():
    # Настройка логирования
    logger = setup_logger(log_file = "logs/solver.log")
    
    try:
        logger.info("Запуск прокотола 2...")


        logger.info("Инициализация констант и начальных значений...")
        init_states, constants = comp_model.initConsts()

        gaps = [0.1, 0.5, 1, 3]

        V = {}
        time = {}
        V_mak = {}

        for gap in gaps:

            logger.info(f"Расчет модели с gap = {gap}")

            constants[58] = 1
            constants[59] = gap
            
            solver = ScipySolver(
                logger = logger,    
                model=comp_model.computeRates,
                t_span=[0, 1],
                y0=init_states,
                args=constants)
            
            voi, states = solver.solve()

            V[gap] = states[0,:]
            time[gap] = voi
            V_mak[gap] = states[29,:]

        for gap in gaps:
            plt.plot(time[gap],V[gap], label = f'G_gap: {gap}')

        plt.xlabel('Время, с')
        plt.ylabel('Потенциал действия, мВ')
        plt.legend()
        plt.savefig('plot.png')

        for gap in gaps:
            plt.plot(time[gap],V_mak[gap], label = f'G_gap: {gap}')

        plt.xlabel('Время, с')
        plt.ylabel('Потенциал действия, мВ')
        plt.legend()
        plt.savefig('plot1.png')

        logger.info("Программа завершена успешна")

    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)
