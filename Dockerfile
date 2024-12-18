
# 3. Deployment (Docker and YAML)
# Dockerfile_model_service
# Dockerfile for model inference service
FROM python:3.8-slim
COPY model_inference_service.py /app/
COPY model_training_pipeline.py /app/
CMD ["python", "-m", "model_inference_service"]

# Dockerfile_data_processor
# Dockerfile for data processing pipeline
FROM python:3.8-slim
COPY data_cleaning.py /app/
COPY feature_engineering.py /app/
CMD ["python", "-m", "data_cleaning"]
