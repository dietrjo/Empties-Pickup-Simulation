# Strategy 1: Pickup as many liters of empties at each address as will be delivered to the customer with the order.
import math

import numpy as np
from scipy.ndimage import standard_deviation

from src.services.csv import create_csv_from_dict
from src.services.random_quantity import get_normal_distribution_quantity
from src.utils.data_loader import load_json

data = load_json('data.json')


def simulate_strategy_1(n: int, tours: list[list[int]]):
    drink_demands = data["customers"]["drink_demands"]

    fulfillment_level_list = []

    full_pickup_num = 0
    pickup_num = 0

    fulfillment_level_graph_values = {key / 2: 0 for key in range(201)}

    for _ in range(n):
        pickup_demands = 0
        pickup_quantity = 0

        for i in range(len(tours)):
            tour = tours[i]

            # if vehicle is not used for delivery
            if len(tour) == 2:
                continue

            for j in range(1, len(tour) - 1):
                drink_demand = drink_demands[tour[j]]
                pickup_demand = get_normal_distribution_quantity()

                pickup_demands += pickup_demand
                pickup_num += 1

                if pickup_demand > drink_demand:
                    pickup_quantity += drink_demand
                else:
                    pickup_quantity += pickup_demand
                    full_pickup_num += 1

        fulfillment_level = pickup_quantity / pickup_demands
        fulfillment_level_list += [fulfillment_level]

        rounded_level = math.ceil(fulfillment_level * 200) / 2
        fulfillment_level_graph_values[rounded_level] += 1

    average_fulfillment_level = sum(fulfillment_level_list) / n
    print(f'Erfüllungsgrad von Strategie 1: {round(average_fulfillment_level * 100, 2)}%')

    standard_deviation_fulfillment_level = standard_deviation(np.array(fulfillment_level_list))
    print(f'Standardabweichung von Strategie 1: {round(standard_deviation_fulfillment_level, 4):.4f}')

    full_pickup_quote = full_pickup_num / pickup_num
    print(f'100% Abholquote von Strategie 1: {round(full_pickup_quote * 100, 2)}%')

    create_csv_from_dict(fulfillment_level_graph_values, "strategy1_fulfilment_distribution.csv")
