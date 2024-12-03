import pandas as pd
import numpy as np

from geopy.distance import great_circle as GC


def get_distance(point1: tuple, point2: tuple) -> float:
    # Air distance in meters:
    dist = GC(point1, point2).km * 1000
    return round(dist, 2)


def create_distance_matrix(coords: list, addresses: list, format='DataFrame', verbose=False):
    # Create empty np-array:
    dist_array = np.empty((len(coords), len(coords)))

    # Compute distances:
    for i in range(0, len(coords)):
        for j in range(i, len(coords)):
            if i < j:
                dist = get_distance(coords[i], coords[j])

                if verbose:
                    print(f"Distance between: {addresses[i]} and {addresses[j]}: {dist} km")

                # Assuming symmetric TSP:
                dist_array[i][j] = dist
                dist_array[j][i] = dist
            elif i == j:
                dist_array[i][i] = 0
            else:
                continue

    if format == 'NumpyArray':
        return dist_array
    else:
        # Create pandas distance matrix:
        return pd.DataFrame(data=dist_array, index=addresses, columns=addresses)
