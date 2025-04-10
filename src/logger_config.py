from loguru import logger
from pathlib import Path
import sys

def setup_logger(log_file: str = None):
    """Настройка логгера с выводом в консоль и файл."""
    
    # Удаляем стандартные обработчики
    logger.remove()  
    
    # Вывод в консоль
    logger.add(
        sys.stdout,
        format="{time:YYYY-MM-DD HH:mm:ss} - {name} - {level} - {message}",
        level="INFO"
    )
    
    # Запись в файл (если указан)
    if log_file:
        Path(log_file).parent.mkdir(exist_ok=True, parents=True)
        logger.add(
            log_file,
            format="{time:YYYY-MM-DD HH:mm:ss} - {name} - {level} - {message}",
            level="INFO",
            rotation="10 MB"  # Автоматическая ротация логов при достижении 10 МБ
        )
    
    return logger