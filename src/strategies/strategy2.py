# Strategy 2: Pickup as many liters of empties at each address as will fit in the delivery vehicle.

from src.services.random_quantity import get_normal_distribution_quantity
from src.utils.data_loader import load_json

data = load_json('data.json')


def simulate_strategy_2(n: int, tours: list[list[int]]):
    vehicle_capacities = data["vehicle_capacities"]
    drink_demands = data["customers"]["drink_demands"]
    other_demands = data["customers"]["other_demands"]

    sum_fulfillment_level = 0

    full_pickup_num = 0
    pickup_num = 0

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
                tour_demand += drink_demands[j]
                tour_demand += other_demands[j]

            vehicle_space = vehicle_capacity - tour_demand

            for j in range(1, len(tour) - 1):
                drink_demand = drink_demands[tour[j]]
                other_demand = other_demands[tour[j]]
                pickup_demand = get_normal_distribution_quantity()

                pickup_demands += pickup_demand
                vehicle_space += drink_demand
                vehicle_space += other_demand
                pickup_num += 1

                if vehicle_space >= pickup_demand:
                    pickup_quantity += pickup_demand
                    vehicle_space -= pickup_demand
                    full_pickup_num += 1
                else:
                    pickup_quantity += vehicle_space
                    vehicle_space = 0

        fulfillment_level = pickup_quantity / pickup_demands
        sum_fulfillment_level += fulfillment_level

    average_fulfillment_level = sum_fulfillment_level / n
    print(f'Erfüllungsgrad von Strategie 2: {round(average_fulfillment_level * 100, 2)}%')

    full_pickup_quote = full_pickup_num / pickup_num
    print(f'100% Abholquote von Strategie 2: {round(full_pickup_quote * 100, 2)}%')
