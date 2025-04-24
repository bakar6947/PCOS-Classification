import os
import logging
from datetime import datetime



# Setup Loagin Files
LOG_FOLDER_FORMAT = f"{datetime.now().strftime('%d_%m_%Y_%H_%M')}"

LOG_FILE_FORMAT = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"


# Create Logs. Directory
log_path = os.path.join(os.getcwd(), 'Logs', LOG_FOLDER_FORMAT)
os.makedirs(log_path, exist_ok=True)

# Create Log File
LOG_FILE = os.path.join(log_path, LOG_FILE_FORMAT)


# Configure Logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='[%(asctime)s] - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
)