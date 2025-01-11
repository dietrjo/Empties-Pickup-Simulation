# Strategy 2: Pickup as many liters of empties at each address as will fit in the delivery vehicle.

from src.services.random_quantity import get_normal_distribution_quantity
from src.utils.data_loader import load_json

data = load_json('data.json')


def simulate_strategy_2(n: int, tours: list[list[int]]):
    vehicle_capacities = data["vehicle_capacities"]
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

            vehicle_capacity = vehicle_capacities[i]

            tour_demand = 0
            for j in range(1, len(tour) - 1):
                tour_demand += demands[j]

            vehicle_space = vehicle_capacity - tour_demand

            for j in range(1, len(tour) - 1):
                demand = demands[tour[j]]
                pickup_demand = get_normal_distribution_quantity(5)

                pickup_demands += pickup_demand
                vehicle_space += demand

                if vehicle_space >= pickup_demand:
                    pickup_quantity += pickup_demand
                    vehicle_space -= pickup_demand
                else:
                    pickup_quantity += vehicle_space
                    vehicle_space = 0

        fulfillment_level = pickup_quantity / pickup_demands
        sum_fulfillment_level += fulfillment_level

    average_fulfillment_level = sum_fulfillment_level / n
    print(f'Erfüllungsgrad von Strategie 2: {round(average_fulfillment_level * 100, 2)}%')