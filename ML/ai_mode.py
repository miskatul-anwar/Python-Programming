import tensorflow as tf
import numpy as np

# Sample Python code
code = """
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(result)
"""

# Preprocessing the code
vocab = list(set(code))
char2idx = {u: i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)
encoded_code = np.array([char2idx[c] for c in code])

# Create training data
input_sequences = []
output_sequences = []
seq_length = 50
for i in range(0, len(encoded_code) - seq_length, 1):
    input_seq = encoded_code[i : i + seq_length]
    output_seq = encoded_code[i + seq_length]
    input_sequences.append(input_seq)
    output_sequences.append(output_seq)

X = np.reshape(input_sequences, (len(input_sequences), seq_length, 1))
X = X / float(len(vocab))
y = tf.keras.utils.to_categorical(output_sequences)

# Build the model
model = tf.keras.Sequential(
    [
        tf.keras.layers.LSTM(256, input_shape=(X.shape[1], X.shape[2])),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(y.shape[1], activation="softmax"),
    ]
)

model.compile(loss="categorical_crossentropy", optimizer="adam")

# Load weights (if model weights exist)
try:
    model.load_weights("model_weights.h5")
except:
    pass

# Train the model
model.fit(X, y, epochs=100, batch_size=64)

# Save weights
model.save_weights("model_weights.h5")


# Function to generate output
def generate_output(model, input_string, seq_length, vocab, char2idx, idx2char):
    output = ""
    code = input_string
    for i in range(100):
        encoded_code = [char2idx[c] for c in code]
        encoded_code = np.reshape(encoded_code, (1, len(encoded_code), 1))
        encoded_code = encoded_code / float(len(vocab))
        prediction = model.predict(encoded_code, verbose=0)
        index = np.argmax(prediction)
        result = idx2char[index]
        seq_in = [idx2char[value] for value in encoded_code[0, :, 0]]
        output += result
        code += result
        code = code[1 : len(code)]

    return output


# Get output for the given code
output = generate_output(model, code, seq_length, vocab, char2idx, idx2char)
print("Output of the given code:", output)
