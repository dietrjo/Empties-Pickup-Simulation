import webbrowser

from src.services.location import get_customer_locations, get_warehouse_location
from src.services.map import create_map
from src.services.tour import get_tours, get_routes_lat_lons


def main():
    customer_locations = get_customer_locations()
    warehouse_location = get_warehouse_location()

    tours, coords = get_tours(warehouse_location, customer_locations)
    routes_lat_lons = get_routes_lat_lons(tours, coords)



    create_map(warehouse_location, customer_locations, routes_lat_lons).save("tour_map.html")
    webbrowser.open("tour_map.html")


if __name__ == '__main__':
    main()
