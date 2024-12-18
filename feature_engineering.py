# Generates features for model training
import data_cleaning as dc

def generate_features(raw_data):
    cleaned_data = dc.clean_data(raw_data)
    features = [{'feature': len(data)} for data in cleaned_data]
    return features

def calculate_statistics(features):
    stats = {
        "min": min(f['feature'] for f in features),
        "max": max(f['feature'] for f in features),
    }
    return stats

