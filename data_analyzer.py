import csv
import os

import numpy as np

from cleaner import clean_all_sectors
from data_service import sectors


def analyze_sector(sector: np.ndarray, sector_number: int):
    min_temperature = np.min(sector)
    max_temperature = np.max(sector)
    mean_temperature = np.mean(sector)
    median_temperature = np.median(sector)
    temperature_range = max_temperature - min_temperature

    return [sector_number, min_temperature, max_temperature, mean_temperature,
            median_temperature, temperature_range]


def process_data_sectors(all_sectors: np.ndarray) -> None:
    result = []
    sector_index = 0

    for sectors_row in all_sectors:
        for sector in sectors_row:
            result.append(analyze_sector(sector, sector_index))
            sector_index += 1

    file_path = os.path.join(os.path.dirname(__file__), "results", "sensors_analysis.csv")
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["sector_index", "min_temperature", "max_temperature",
                         "mean_temperature", "median_temperature", "temperature_range"])
        writer.writerows(result)


if __name__ == "__main__":
    clean_all_sectors(sectors)
    process_data_sectors(sectors)
    print("Аналіз секторів збережено")
