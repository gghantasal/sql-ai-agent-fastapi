# src/utils/logger.py
import logging
import os

def setup_logging():
    log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
    numeric_log_level = getattr(logging, log_level_str, logging.INFO)

    logging.basicConfig(
        level=numeric_log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )
    # Optional: Set higher log level for some noisy libraries if needed
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)

# Call this at the start of your application
setup_logging()
logger = logging.getLogger(__name__)