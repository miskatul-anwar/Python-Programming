import torch
import torch.nn as nn
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
y = torch.tensor(output_sequences)


# Define the model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        out = self.fc(lstm_out[:, -1, :])
        return out


# Initialize the model
model = LSTMModel(input_size=1, hidden_size=256, output_size=len(vocab))

# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Train the model
num_epochs = 100
for epoch in range(num_epochs):
    inputs = torch.Tensor(X)
    outputs = model(inputs)
    loss = criterion(outputs, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")


# Function to generate output
def generate_output(model, input_string, seq_length, vocab, char2idx, idx2char):
    output = ""
    code = input_string
    for i in range(100):
        encoded_code = [char2idx[c] for c in code]
        encoded_code = np.reshape(encoded_code, (1, len(encoded_code), 1))
        encoded_code = torch.tensor(
            encoded_code / float(len(vocab)), dtype=torch.float32
        )
        prediction = model(encoded_code)
        index = torch.argmax(prediction).item()
        result = idx2char[index]
        output += result
        code += result
        code = code[1 : len(code)]

    return output


# Get output for the given code
output = generate_output(model, code, seq_length, vocab, char2idx, idx2char)
print("Output of the given code:", output)
