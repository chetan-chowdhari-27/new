import logging
import os
# import sys
from datetime import datetime

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # name of log file
log_path = os.path.join(os.getcwd(),"logs",log_file)  # were we need create log file
os.makedirs(log_path,exist_ok=True)  # creating files 

log_file_path = os.path.join(log_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__ == "__main__":
    logging.info('the  script is running')