import csv
import os

import numpy as np


file_path = os.path.join(os.path.dirname(__file__), "data_files", "sensors.csv")

data = []
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append([float(value) for value in row])

data = np.array(data)

sectors = data.reshape(12, 10, 14, 10).transpose(0, 2, 1, 3)

if __name__ == "__main__":
    print("Data:", data.shape)
    print("Sectors:", sectors.shape)
    print("View:", np.shares_memory(data, sectors))
