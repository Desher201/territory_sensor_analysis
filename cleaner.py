import numpy as np


def clean_sector(sector: np.ndarray) -> None:
    median = np.nanmedian(sector)

    for row in range(len(sector)):
        for col in range(len(sector[row])):
            value = sector[row][col]
            if np.isnan(value) or abs(value - median) > 10:
                sector[row][col] = median


def clean_all_sectors(all_sectors: np.ndarray) -> None:
    for sectors_row in all_sectors:
        for sector in sectors_row:
            clean_sector(sector)
