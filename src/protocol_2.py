# Расчет до 10 с.
# Поварьировать g_gap = [0.1, 0.5, 1, 3]
# График (число g_gap, частота стимуляции)
# График (число g_gap, максимум ПД)
# График (число g_gap, минимум ПД)
# График (число g_gap, амрлитула ПД)
# График (число g_gap, длительность потенциала действия)
# Поварьировать number_macrofag = [1, 2, 3]


from scipy_solver import ScipySolver
from scipy.signal import argrelmax, argrelmin
import model as comp_model
import matplotlib.pyplot as plt
import numpy as np


def solve_protocol(logger, gaps, number_macrofags, t_span):
    try:
        logger.info("Запуск расчетов...")


        logger.info("Инициализация констант и начальных значений...")
        init_states, constants = comp_model.initConsts()

        V = {}
        time = {}
        V_mak = {}

        for gap in gaps:
            V_number = {}
            t_number = {}
            V_mac_number = {}
            for number_macrofag in number_macrofags:

                logger.info(f"Расчет модели с gap = {gap} и number_macrofag = {number_macrofag}")

                constants[58] = number_macrofag
                constants[59] = gap
                
                solver = ScipySolver(
                    logger = logger,    
                    model=comp_model.computeRates,
                    t_span=t_span,
                    y0=init_states,
                    args=constants)
                
                voi, states = solver.solve()
                V_number[number_macrofag] = states[0,:]
                t_number[number_macrofag] = voi
                V_mac_number[number_macrofag] = states[29,:]

            V[gap] = V_number
            time[gap] = t_number
            V_mak[gap] = V_mac_number

        return V, time, V_mak
    
    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)

def AP_conf(logger, V, time, V_mak, gaps, number_macrofags):
    try:
        logger.info("Рачет характеристик ПД...")
        V_max = {}
        V_min = {}
        characteristics = {}
        for gap in gaps:
            V_max_number = {}
            V_min_number = {}
            characteristics_number = {}
            for number_macrofag in number_macrofags:

                maximum_V_index = argrelmax(V[gap][number_macrofag])
                maximum_V = V[gap][number_macrofag][maximum_V_index]
                maximum_V_time = time[gap][number_macrofag][maximum_V_index]
                V_max_number[number_macrofag] = {'index': maximum_V_index, 'maximum': maximum_V, 'time': maximum_V_time}

                print('Индексы максимумов V', maximum_V_index)
                print('Максимумы V', maximum_V)
                print('Время локальных максимумов', maximum_V_time)

                minimum_V_index = argrelmin(V[gap][number_macrofag])
                minimum_V = V[gap][number_macrofag][minimum_V_index]
                minimum_V_time = time[gap][number_macrofag][minimum_V_index]
                V_min_number[number_macrofag] = {'index': minimum_V_index, 'minimum': minimum_V, 'time': minimum_V_time}

                print('Индексы минимумов V', minimum_V_index)
                print('Минимумы V', minimum_V)
                print('Время локальных минимумов', minimum_V_time)

                characteristics_number[number_macrofag] = {'ampl': maximum_V[-1]-minimum_V[-1], 'period': maximum_V_time[-1]-maximum_V_time[-2]}
                print('Амплитуда потенциала действия',characteristics_number[number_macrofag]['ampl'], 'Период', characteristics_number[number_macrofag]['period'])

            V_max[gap] = V_max_number
            V_min[gap] = V_min_number
            characteristics[gap] = characteristics_number

        return V_max, V_min, characteristics

    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)

def plot_AP(logger, gaps, number_macrofags, V, time, V_mak, V_max, V_min, characteristics):
    try:
        logger.info("Пострение графиков")
        fig, ax = plt.subplots()        
        for gap in gaps:
            for number_macrofag in number_macrofags:
                ax.plot(time[gap][number_macrofag],V[gap][number_macrofag], label = f'G_gap: {gap}, nu: {number_macrofag}, nu: {number_macrofag}, Pr: {characteristics[gap][number_macrofag]['period']:.2f} s.')
                ax.scatter(V_max[gap][number_macrofag]['time'],V_max[gap][number_macrofag]['maximum'])
                ax.scatter(V_min[gap][number_macrofag]['time'],V_min[gap][number_macrofag]['minimum'])
                ax.plot([V_max[gap][number_macrofag]['time'][-1], V_max[gap][number_macrofag]['time'][-1]],
                        [V_max[gap][number_macrofag]['maximum'][-1],V_max[gap][number_macrofag]['maximum'][-1]-characteristics[gap][number_macrofag]['ampl']],
                        color = 'red')
        ax.set_xlabel('Время, с')
        ax.set_ylabel('Потенциал действия, мВ')
        ax.legend()
        plt.savefig('plot.png')
        plt.show()

        fig, ax = plt.subplots()
        for gap in gaps:
            ax.plot(time[gap][number_macrofag],V_mak[gap][number_macrofag], label = f'G_gap: {gap}')

        ax.set_xlabel('Время, с')
        ax.set_ylabel('Потенциал макрофага, мВ')
        ax.legend()
        plt.savefig('plot1.png')
        plt.show()
    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)

def main_protocol(logger):
    try:
        logger.info("Запуск прокотола...")
        # Списки с значениями gap и number_macrofag которые мы хотим посчитать
        
        gaps = [0.1, 1.0]
        number_macrofags = [1]
        # Списки с значениями time [time_min, time_max]
        t_span = [0, 1]

        logger.info(f"Значения gaps: {gaps}")
        logger.info(f"Значения number_macrofags: {number_macrofags}")

        V, time, V_mak = solve_protocol(logger, gaps, number_macrofags, t_span)
        V_max, V_min, characteristics = AP_conf(logger, V, time, V_mak, gaps, number_macrofags)
        plot_AP(logger, gaps, number_macrofags, V, time, V_mak, V_max, V_min, characteristics)

        logger.info("Программа завершена успешно") 

    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)