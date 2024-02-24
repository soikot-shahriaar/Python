import os

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"data/data_{i+1}")