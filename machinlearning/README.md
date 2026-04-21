# Machine Learning - MNIST Classification

A simple machine learning project that trains a neural network on the MNIST handwritten digit dataset using TensorFlow and Docker.

## Overview

This project demonstrates a basic neural network implementation that:
- Loads and preprocesses the MNIST dataset
- Trains a single-layer dense neural network for digit classification
- Saves the trained model for future use
- Runs entirely in a Docker container

## Files Structure

```
machinlearning/
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose setup
├── hello_world.py         # Main ML script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Components

### hello_world.py
The main script that:
- Loads the MNIST dataset using TensorFlow/Keras
- Preprocesses the data (normalization and reshaping)
- Defines a single-layer neural network with softmax activation
- Trains the model using stochastic gradient descent
- Evaluates the model on test data
- Saves the trained model as `mnist_model.keras`

### Dockerfile
Creates a Python 3.11 environment with:
- TensorFlow installed from requirements.txt
- Working directory set to `/webapp`
- All necessary system dependencies

### docker-compose.yml
- Builds the Docker image from the current directory
- Runs the training script automatically
- Mounts the current directory to `/webapp` in the container
- Uses an external volume named `webapp`

## Usage

### Prerequisites
- Docker installed on your system
- Docker Compose (optional but recommended)

### Running the Project

#### Option 1: Using Docker Compose (Recommended)
```bash
# Make sure you're in the machinlearning directory
cd machinlearning

# Create the external volume (if it doesn't exist)
docker volume create webapp

# Run the training
docker-compose up --build
```

#### Option 2: Using Docker directly
```bash
# Build the Docker image
docker build -t ml-mnist .

# Run the container
docker run --rm -v $(pwd):/webapp ml-mnist
```

## Model Details

- **Architecture**: Single dense layer with 10 output neurons
- **Input Shape**: 784 features (28x28 flattened MNIST images)
- **Activation**: Softmax (for multi-class classification)
- **Optimizer**: Stochastic Gradient Descent (learning rate: 0.05)
- **Loss Function**: Categorical Crossentropy
- **Batch Size**: 100
- **Epochs**: 10

## Expected Output

The script will:
1. Display training progress for 10 epochs
2. Show the current directory contents
3. Print the final test accuracy
4. Save the trained model to `/webapp/mnist_model.keras`

Typical accuracy for this simple model is around 92% on the MNIST test set.

## Model Persistence

After training, the model is saved as `mnist_model.keras` in the webapp directory. This file contains:
- Model architecture
- Trained weights
- Optimizer state

You can load this model later for inference using:
```python
import tensorflow as tf
model = tf.keras.models.load_model('mnist_model.keras')
```

## Dependencies

- **tensorflow**: Core machine learning framework
- **numpy**: Required for numerical operations (installed with TensorFlow)

## Customization

You can modify the training parameters in `hello_world.py`:
- Change `batch_size` for different batch training
- Adjust `epochs` for longer/shorter training
- Modify `learning_rate` in the SGD optimizer
- Experiment with different model architectures

## Troubleshooting

1. **Docker volume issues**: Make sure the `webapp` volume exists: `docker volume create webapp`
2. **Memory errors**: Reduce batch size if you encounter memory issues
3. **Permission issues**: The Dockerfile includes `C_FORCE_ROOT=1` to handle permission constraints

## Learning Objectives

This project serves as an introduction to:
- Basic neural network concepts
- TensorFlow/Keras API usage
- Docker containerization for ML projects
- Model training and persistence
- MNIST dataset handling