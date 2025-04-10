from logger_config import setup_logger
from scipy_solver import ScipySolver
import model as comp_model
import matplotlib.pyplot as plt
import numpy as np

from protocol_1 import exp_1


def main():
    # Настройка логирования
    logger = setup_logger(log_file = "logs/solver.log")
    
    try:
        logger.info("Запуск программы...")


        logger.info("Инициализация констант и начальных значений...")
        init_states, constants = comp_model.initConsts()

        solver = ScipySolver(
            logger = logger,    
            model=comp_model.computeRates,
            t_span=[0, 1],
            y0=init_states,
            args=constants)
        
        voi, states = solver.solve()

        # Расчет алгебраических переменных
        logger.info("Расчет алгебраических переменных...")
        algebraic = comp_model.computeAlgebraic(constants, states, voi)

        plt.plot(voi,states[0,:])
        plt.savefig('plot.png')

        logger.info("Программа завершена успешна")

    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)


if __name__ == "__main__":
    # main()

    number_cell = [0, 1]
    time = [0, 1]

    exp_1(t_span=time, number_macrofags=number_cell)