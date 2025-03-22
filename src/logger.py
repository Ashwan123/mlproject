import logging
import os
from datetime import datetime

# Create a unique log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path to the logs directory
logs_directory = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_directory, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE)

# Set up logging to file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Add a console handler so logs appear in the console too
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # You can adjust the level to DEBUG if needed

# Set the format for console logs
formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Add the console handler to the root logger
logging.getLogger().addHandler(console_handler)

# Test logging to ensure everything is set up
logging.info("Logger setup complete. Log file path: %s", LOG_FILE_PATH)
logging.info("This is a test log message.")
