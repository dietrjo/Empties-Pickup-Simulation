import webbrowser

from src.services.location import get_customer_locations, get_warehouse_location
from src.services.map import create_map
from src.services.tour import get_tours, get_routes_lat_lons
from src.strategies.strategy1 import simulate_strategy_1
from src.strategies.strategy2 import simulate_strategy_2


def main():
    print("Read in locations... ", end="")
    customer_locations = get_customer_locations()
    warehouse_location = get_warehouse_location()
    print (u'\u2713')

    print("\nGenerate tours...")
    tours, coords = get_tours(warehouse_location, customer_locations)
    routes_lat_lons = get_routes_lat_lons(tours, coords)

    print("\nSimulate pickup strategies...")
    simulate_strategy_1(100000, tours)
    simulate_strategy_2(100000, tours)

    print("\nCreate maps... ", end="")
    for i in range(len(routes_lat_lons)):
        create_map(warehouse_location, customer_locations, routes_lat_lons[i]).save(f'tour_map{i+1}.html')
        webbrowser.open(f'tour_map{i+1}.html')
    webbrowser.open('tour_map0.html')
    print (u'\u2713')


if __name__ == '__main__':
    main()
