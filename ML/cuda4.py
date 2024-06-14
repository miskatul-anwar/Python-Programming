import torch

# check if cuda is available
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
print(device)

# Create tensors and move them to the selected device
a = torch.arange(100000, device=device) * 10

# Synchronize CUDA operations
torch.cuda.synchronize()

# Print the tensors
print(a)
