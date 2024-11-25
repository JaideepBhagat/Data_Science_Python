import numpy as np
import matplotlib.pyplot as plt


class SGDOptimizer:
    def __init__(self, learning_rate=0.01, batch_size=1):
        """
        Initialize SGD optimizer.

        Parameters:
            learning_rate: Step size for parameter updates
            batch_size: Number of samples per batch (1 for pure SGD)
        """
        self.learning_rate = learning_rate
        self.batch_size = batch_size

    def generate_batches(self, X, y):
        """Create mini-batches from the data"""
        indices = np.random.permutation(len(X))
        for i in range(0, len(X), self.batch_size):
            batch_idx = indices[i:i + self.batch_size]
            yield X[batch_idx], y[batch_idx]


class LinearRegressionSGD:
    def __init__(self, learning_rate=0.01, batch_size=1, epochs=100):
        self.lr = learning_rate
        self.epochs = epochs
        self.optimizer = SGDOptimizer(learning_rate, batch_size)
        self.loss_history = []
        self.weights = None
        self.bias = None

    def initialize_parameters(self, n_features):
        """Initialize model parameters"""
        self.weights = np.zeros(n_features)
        self.bias = 0

    def compute_gradients(self, X_batch, y_batch, y_pred):
        """Compute gradients for the current batch"""
        m = len(X_batch)
        dw = (1 / m) * np.dot(X_batch.T, (y_pred - y_batch))
        db = (1 / m) * np.sum(y_pred - y_batch)
        return dw, db

    def fit(self, X, y):
        """Train the model using SGD"""
        self.initialize_parameters(X.shape[1])

        print("Starting training...")
        for epoch in range(self.epochs):
            epoch_loss = 0
            batch_count = 0

            # Process mini-batches
            for X_batch, y_batch in self.optimizer.generate_batches(X, y):
                # Forward pass
                y_pred = np.dot(X_batch, self.weights) + self.bias

                # Compute gradients
                dw, db = self.compute_gradients(X_batch, y_batch, y_pred)

                # Update parameters
                self.weights -= self.lr * dw
                self.bias -= self.lr * db

                # Compute loss for this batch
                batch_loss = np.mean((y_pred - y_batch) ** 2)
                epoch_loss += batch_loss
                batch_count += 1

            # Average loss for the epoch
            avg_epoch_loss = epoch_loss / batch_count
            self.loss_history.append(avg_epoch_loss)

            if epoch % 10 == 0:
                print(f"Epoch {epoch}, Loss: {avg_epoch_loss:.6f}")

    def predict(self, X):
        """Make predictions"""
        return np.dot(X, self.weights) + self.bias


# Generate synthetic data for demonstration
def generate_data(n_samples=1000):
    np.random.seed(42)
    X = np.random.randn(n_samples, 2)  # 2 features
    true_weights = np.array([2.0, -3.5])
    true_bias = 1.0
    y = np.dot(X, true_weights) + true_bias + np.random.randn(n_samples) * 0.1
    return X, y


# Compare SGD with different batch sizes
def compare_batch_sizes():
    X, y = generate_data()

    batch_sizes = [1, 32, len(X)]  # SGD, Mini-batch, Full batch
    models = []

    plt.figure(figsize=(15, 5))

    for i, batch_size in enumerate(batch_sizes):
        model = LinearRegressionSGD(
            learning_rate=0.01,
            batch_size=batch_size,
            epochs=100
        )

        model.fit(X, y)
        models.append(model)

        plt.subplot(1, 3, i + 1)
        plt.plot(model.loss_history)
        plt.title(f'Batch Size = {batch_size}')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.grid(True)

    plt.tight_layout()
    plt.show()

    return models


# Run comparison and print results
models = compare_batch_sizes()

# Print final parameters for each model
batch_sizes = [1, 32, len(generate_data()[0])]
true_weights = np.array([2.0, -3.5])
true_bias = 1.0

print("\nComparison of Final Parameters:")
print(f"True weights: {true_weights}, True bias: {true_bias}")
print("-" * 50)

for model, batch_size in zip(models, batch_sizes):
    print(f"\nBatch size: {batch_size}")
    print(f"Learned weights: {model.weights.round(4)}")
    print(f"Learned bias: {model.bias.round(4)}")
    print(f"Final loss: {model.loss_history[-1]:.6f}")