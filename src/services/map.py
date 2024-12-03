import folium

from geopy import Nominatim

import osmnx as ox

from src.services.location import Location
from src.utils.data_loader import load_json
from src.utils.distance_matrix import create_distance_matrix
from src.utils.nearest_neighbor import nearest_neighbor

geolocator = Nominatim(user_agent="TSP_Jena")
G = ox.graph_from_place("Jena, Germany", network_type="drive_service", simplify=False)


def get_customer_locations() -> list:
    cust_locations = []
    for address in load_json('data/customer_addresses.json'):
        loc = geolocator.geocode(address)

        if loc is None:
            print(f"Address couldn't be located: {address}")
            break

        cust_locations += [Location(address, (loc.latitude, loc.longitude))]
    return cust_locations


def get_warehouse_location() -> Location:
    warehouse_address = load_json('data/warehouse_address.json')
    loc = geolocator.geocode(warehouse_address)
    return Location(warehouse_address, (loc.latitude, loc.longitude))


def get_tour(warehouse_location, customer_locations) -> list:
    addresses = [warehouse_location.address] + [loc.address for loc in customer_locations]
    coords = [warehouse_location.coords] + [loc.coords for loc in customer_locations]

    dist_matrix_np = create_distance_matrix(addresses=addresses, coords=coords, verbose=False, format='NumpyArray')
    # dist_matrix_df = create_distance_matrix(addresses=addresses, coords=coords, verbose=False, format='DataFrame')

    # tour -> array with the indexes of the locations
    tour = nearest_neighbor(dist_matrix_np)
    tour_coords = [coords[i] for i in tour]

    route_lat_lons = []
    for i in range(0, len(tour) - 1):
        start_node = ox.nearest_nodes(G, tour_coords[i][1], tour_coords[i][0])
        end_node = ox.nearest_nodes(G, tour_coords[i + 1][1], tour_coords[i + 1][0])

        route = ox.shortest_path(G, start_node, end_node)
        route_lat_lons.append([(G.nodes[node]['y'], G.nodes[node]['x']) for node in route])

    return route_lat_lons


def create_map():
    customer_locations = get_customer_locations()
    warehouse_location = get_warehouse_location()
    tour = get_tour(warehouse_location, customer_locations)

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

    # Create Tour
    for route_coords in tour:
        folium.PolyLine(
            route_coords,
            color="black",
            weight=3
        ).add_to(tour_map)

    return tour_map
