# Nearest neigbor heuristic to find a route for the tour
def nearest_neighbor(distance_matrix: list) -> list:
    tour = [0]
    current_location = 0
    unscheduled_locations = [i for i in range(1, len(distance_matrix))]

    while unscheduled_locations:
        min_distance = 100000000000000  # sufficiently large number
        min_distance_index = -1
        for i in unscheduled_locations:
            if min_distance > distance_matrix[current_location][i] and i != current_location:
                min_distance = distance_matrix[current_location][i]
                min_distance_index = i

        current_location = min_distance_index
        unscheduled_locations.remove(min_distance_index)
        tour += [min_distance_index]

    tour += [0]

    return tour


def test():
    tour = nearest_neighbor([[0, 4, 3, 1, 6],
                             [4, 0, 3, 6, 9],
                             [3, 3, 0, 3, 7],
                             [1, 6, 3, 0, 3],
                             [6, 9, 7, 3, 0]])
    print(tour)


if __name__ == '__main__':
    test()
