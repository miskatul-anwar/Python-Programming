import pyfiglet
import torch
import time

device = torch.device("cuda")
matrix_size = 32 * 512
x = torch.randn(matrix_size, matrix_size)
y = torch.randn(matrix_size, matrix_size)
font = pyfiglet.figlet_format("CPU")
print(font)
print()
start = time.time()
result = torch.matmul(x, y)
print("Time:", time.time() - start)
print("verify:", result.device)

x_gpu = x.to(device)
y_gpu = y.to(device)
torch.cuda.synchronize()
font = pyfiglet.figlet_format("GPU")
print(font)
print()
start = time.time()
result_gpu = torch.matmul(x_gpu, y_gpu)
print("Time:", time.time() - start)
print("verify:", result_gpu.device)
