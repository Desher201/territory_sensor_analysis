import csv
import os

import numpy as np

from data_service import sectors
from cleaner import clean_all_sectors
from problem_analyzer import problem_analyzer
from data_analyzer import process_data_sectors


def all_sectors_analizer(all_sectors):
    temperatures = []
    sector_index = 0

    for sectors_row in all_sectors:
        for sector in sectors_row:
            temperatures.append([sector_index, np.mean(sector)])
            sector_index += 1

    temperatures.sort(key=lambda a: a[1])
    cold = temperatures[:10]
    hot = temperatures[-10:][::-1]

    average = np.mean([a[1] for a in temperatures])
    other = temperatures[10:-10]
    other.sort(key=lambda a: abs(a[1] - average))
    normal = other[:30]

    result = []
    for sector in cold:
        result.append([sector[0], "cold"])
    for sector in hot:
        result.append([sector[0], "hot"])
    for sector in normal:
        result.append([sector[0], "near_average"])

    file_path = os.path.join(os.path.dirname(__file__), "results", "all_sectors.csv")
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["sector_index", "category"])
        writer.writerows(result)

    return result


if __name__ == "__main__":
    problems = problem_analyzer(sectors)
    clean_all_sectors(sectors)
    process_data_sectors(sectors)
    result = all_sectors_analizer(sectors)

    print("Секторів:", len(sectors) * len(sectors[0]))
    print("Некоректних значень:", sum(row[4] for row in problems))
    print("Холодних:", len([row for row in result if row[1] == "cold"]))
    print("Теплих:", len([row for row in result if row[1] == "hot"]))
    print("Близьких до середньої:", len([row for row in result if row[1] == "near_average"]))
