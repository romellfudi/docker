import tensorflow as tf

# Load dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Preprocess
x_train = x_train.reshape(-1, 784).astype("float32") / 255.0
x_test = x_test.reshape(-1, 784).astype("float32") / 255.0

y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Define model (equivalent to W, b, softmax)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="softmax", input_shape=(784,))
])

# Compile (loss = cross entropy, optimizer = gradient descent)
model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.05),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# Train (replaces session loop)
model.fit(x_train, y_train, batch_size=100, epochs=10)

# Evaluate
loss, accuracy = model.evaluate(x_test, y_test)
# print current path and make a ls command to show the saved model file
import os
print("Current path:", os.getcwd())
print("Files in current directory:")
os.system("ls")


print("The Accuracy:", accuracy)
model.save(f"/webapp/mnist_model.keras")
print("Model saved as mnist_model.keras")