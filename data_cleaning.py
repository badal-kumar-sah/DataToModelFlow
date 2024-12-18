# Cleans raw data
import logging_configuration as log

def clean_data(raw_data):
    log.setup_logging()
    cleaned_data = [data.strip() for data in raw_data if data]
    log.log_event("Data cleaned successfully")
    return cleaned_data

def split_data(cleaned_data):
    return cleaned_data[:len(cleaned_data)//2], cleaned_data[len(cleaned_data)//2:]
