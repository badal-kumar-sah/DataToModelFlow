# Handles data uploads
import logging_configuration as log

def upload_data(data):
    log.setup_logging()
    log.log_event("Uploading data")
    return f"Uploaded {len(data)} items"
