import os

for i in range(0, 100):
    os.rename(f"data/data_{i+1}", f"data/data_day_ {i+1}")