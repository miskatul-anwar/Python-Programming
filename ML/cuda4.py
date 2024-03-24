import torch

# check if cuda is available
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
print(device)
torch.cuda.synchronize()
for i in range(100000):
    print(i * 10)
