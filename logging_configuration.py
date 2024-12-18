# Configures logging settings
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)

def log_event(event):
    logging.info(f"Event: {event}")
