import logging
import os

def setup_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        filename="logs/system.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log_success(file_name, category):
    logging.info(f"Processed: {file_name} | Category: {category}")

def log_error(file_name, error):
    logging.error(f"Error processing {file_name}: {error}")