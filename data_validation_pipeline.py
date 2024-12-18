# Validates processed data
import feature_engineering as fe

def validate_data(raw_data):
    features = fe.generate_features(raw_data)
    if not all('feature' in f for f in features):
        raise ValueError("Validation failed: Missing features")
    stats = fe.calculate_statistics(features)
    return stats
