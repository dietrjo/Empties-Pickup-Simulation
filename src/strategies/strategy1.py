# Strategy 1: Pickup as many liters of empties at each address as will be delivered to the customer with the order.

from src.services.random_quantity import get_normal_distribution_quantity
from src.utils.data_loader import load_json

data = load_json('data.json')


def simulate_strategy_1(n: int, tours: list[list[int]]):
    demands = data["customers"]["demands"]

    sum_fulfillment_level = 0

    for _ in range(n):
        pickup_demands = 0
        pickup_quantity = 0

        for i in range(len(tours)):
            tour = tours[i]

            # if vehicle is not used for delivery
            if len(tour) == 2:
                continue

            for j in range(1, len(tour) - 1):
                demand = demands[tour[j]]
                pickup_demand = get_normal_distribution_quantity(5000)

                pickup_demands += pickup_demand
                if pickup_demand >= demand:
                    pickup_quantity += demand
                else:
                    pickup_quantity += pickup_demand

        fulfillment_level = pickup_quantity / pickup_demands
        sum_fulfillment_level += fulfillment_level

    average_fulfillment_level = sum_fulfillment_level / n
    print(f'Erfüllungsgrad von Strategie 1: {round(average_fulfillment_level * 100, 2)}%')
