from scipy.integrate import solve_ivp
import logging

class ScipySolver:
    def __init__(self, model, t_span, y0, logger, **kwargs):
        self.logger = logger
        self.model = model
        self.t_span = t_span
        self.y0 = y0
        self.kwargs = kwargs
        self.logger.info(f"Инициализирован решатель для интервала {t_span}")

    def solve(self):
        try:
            self.logger.debug("Начало решения ОДУ...")
            solution = solve_ivp(
                fun=self.model,
                t_span=self.t_span,
                y0=self.y0,
                **self.kwargs
            )
            self.logger.info(f"Решение завершено. Шагов: {len(solution.t)}")
            return solution.t, solution.y
        except Exception as e:
            self.logger.error(f"Ошибка: {str(e)}", exc_info=True)
            raise