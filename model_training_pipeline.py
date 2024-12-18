# Trains a machine learning model
import feature_engineering as fe

def train_model(raw_data):
    features = fe.generate_features(raw_data)
    model = f"TrainedModel_with_{len(features)}_features"
    return model

def save_model(model):
    with open("model_file.pkl", "w") as f:
        f.write(model)
    return "Model saved"
