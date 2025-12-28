from src.datascience.logger import logging
from src.datascience.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("The execution started")

    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Customer exception occurred")
        raise CustomException(e, sys)