import folium

from geopy import Nominatim

from src.services.location import Location
from src.utils.data_loader import load_json

geolocator = Nominatim(user_agent="TSP_Muenster")


def get_customer_locations() -> list:
    customer_locations = []
    for address in load_json('data/customer_addresses.json'):
        loc = geolocator.geocode(address)

        if loc is None:
            print(f"Address couldn't be located: {address}")
            break

        customer_locations += [Location(address, (loc.latitude, loc.longitude))]
    return customer_locations


def get_warehouse_location() -> Location:
    warehouse_address = load_json('data/warehouse_address.json')
    loc = geolocator.geocode(warehouse_address)
    return Location(warehouse_address, (loc.latitude, loc.longitude))


def generate_map():
    customer_locations = get_customer_locations()
    warehouse_location = get_warehouse_location()

    tour_map = folium.Map(location=warehouse_location.coords, zoom_start=14, tiles='OpenStreetMap')

    # Create warehouse icon:
    folium.Marker(
        location=warehouse_location.coords,
        icon=folium.Icon(color='green', icon='industry', prefix='fa'),
        popup=warehouse_location.address,
        tooltip=warehouse_location.address,
        draggable=False
    ).add_to(tour_map)

    # Create customer address icons:
    for location in customer_locations:
        folium.Marker(
            location=location.coords,
            icon=folium.Icon(color='darkblue', icon='home'),
            popup=location.address,
            tooltip=location.address,
            draggable=False
        ).add_to(tour_map)

    return tour_map
