# Provides inference based on the trained model
import model_training_pipeline as mt

def infer(raw_data):
    model = mt.train_model(raw_data)
    predictions = [f"{model}_predict_{data}" for data in raw_data]
    return predictions

def batch_infer(raw_batches):
    return {f"Batch_{i}": infer(batch) for i, batch in enumerate(raw_batches)}
