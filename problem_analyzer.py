import csv
import os

import numpy as np

from data_service import sectors


def problem_analyzer(datas):
    result = []
    sector_index = 0

    for sectors_row in datas:
        for sector in sectors_row:
            median = np.nanmedian(sector)
            nan_count = 0
            too_low_count = 0
            too_high_count = 0

            for row in sector:
                for value in row:
                    if np.isnan(value):
                        nan_count += 1
                    elif value < median - 10:
                        too_low_count += 1
                    elif value > median + 10:
                        too_high_count += 1

            invalid_count = nan_count + too_low_count + too_high_count
            result.append([sector_index, nan_count, too_low_count, too_high_count, invalid_count])
            sector_index += 1

    file_path = os.path.join(os.path.dirname(__file__), "results", "sensors_problems.csv")
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["sector_index", "nan_count", "too_low_count", "too_high_count", "invalid_count"])
        writer.writerows(result)

    return result


if __name__ == "__main__":
    result = problem_analyzer(sectors)
    print("Секторів:", len(result))
    print("Некоректних значень:", sum(row[4] for row in result))
