# core/logger.py
from loguru import logger
import sys

logger.remove()  # Clear the default handler to avoid duplication

logger.add(sys.stdout, colorize=True, level="DEBUG", backtrace=True, diagnose=True,
           format="<green>{time}</green> | <level>{level}</level> | <cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")
