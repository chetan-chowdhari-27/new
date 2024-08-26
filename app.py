# # # from src.ml_project.logger import logging
from src.mlproject.logger import logging
import sys
from src.mlproject.exception import CustomException



if __name__ == "__main__":
    logging.info('the  script is running')

    try:
        pass
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)