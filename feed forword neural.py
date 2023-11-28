import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Sample data
# XOR logic gate
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]

# Build the model
model = Sequential()
model.add(Dense(2, input_dim=2, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Make predictions
predictions = model.predict(X)

# Print predictions
for i in range(len(X)):
    print(f"Input: {X[i]}, Predicted Output: {predictions[i][0]:.4f}")

# Evaluate the model
loss, accuracy = model.evaluate(X, y)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
