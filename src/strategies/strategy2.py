# Strategy 1: Pickup as many liters of empties at each address as will be delivered to the customer with the order.

from src.utils.data_loader import load_json

data = load_json('data.json')


def simulate_strategy_1(n: int, tours: list[list[int]]):
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

        fulfillment_level = pickup_quantity / pickup_demands
        sum_fulfillment_level += fulfillment_level

    average_fulfillment_level = sum_fulfillment_level / n
