import tensorflow as tf
from tensorflow.keras import layers, models
import os

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0
x_train = tf.expand_dims(x_train, -1)
x_test = tf.expand_dims(x_test, -1)

model = models.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax") 
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("Treinando o modelo (isso pode demorar uns minutinhos)...")
model.fit(x_train, y_train, epochs=5, validation_split=0.1)

loss, acc = model.evaluate(x_test, y_test)
print(f"Acurácia no teste: {acc:.4f}")

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "..", "model", "model.h5")

model.save(model_path)
print(f"Modelo salvo com sucesso em: {model_path}!")