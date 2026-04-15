def train_model():
    print("Initializing GPU...")
    print("Loading data...")
    # Force a failure
    raise Exception("CUDA out of memory! GPU allocation failed.")
    return 0.95

if __name__ == "__main__":
    train_model()
