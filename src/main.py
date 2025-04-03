from utils.logger_config import setup_logger
from solvers.scipy_solver import ScipySolver
from model.lotka_volterra import lotka_volterra

def main():
    # Настройка логирования
    logger = setup_logger("main", log_file="logs/solver.log")
    
    try:
        logger.info("Запуск программы...")

        solver = ScipySolver(
            logger = logger,    
            model=lotka_volterra,
            t_span=[0, 50],
            y0=[10, 5],
            method="RK45"
            )
        t, y = solver.solve()

        logger.info("Программа завершена успешно")

    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)

if __name__ == "__main__":
    main()