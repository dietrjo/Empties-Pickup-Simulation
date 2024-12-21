import osmnx as ox

from src.services.location import Location
from src.utils.data_loader import load_json
from src.utils.distance_matrix import create_distance_matrix
from src.utils.or_tools_cvrp import solve_cvrp

G = ox.graph_from_place("Jena, Germany", network_type="drive_service", simplify=False)
data = load_json('data.json')


def get_tours(warehouse_location, customer_locations) -> (list[list[int]], list[Location]):
    addresses = [warehouse_location.address] + [loc.address for loc in customer_locations]
    coords = [warehouse_location.coords] + [loc.coords for loc in customer_locations]

    dist_matrix_np = create_distance_matrix(addresses=addresses, coords=coords, verbose=False, format='NumpyArray')
    # dist_matrix_df = create_distance_matrix(addresses=addresses, coords=coords, verbose=False, format='DataFrame')

    # tours -> array with arrays with the indexes of the locations
    tours = solve_cvrp(dist_matrix_np)

    return tours, coords

def get_routes_lat_lons(tours, coords) -> list[list[list[tuple[int, int]]]]:
    tours_coords = [[coords[i] for i in tour] for tour in tours]

    routes_lat_lons = []
    for tour in tours_coords:
        route_lat_lons = []
        for i in range(0, len(tour) - 1):
            start_node = ox.nearest_nodes(G, tour[i][1], tour[i][0])
            end_node = ox.nearest_nodes(G, tour[i + 1][1], tour[i + 1][0])

            route = ox.shortest_path(G, start_node, end_node)
            route_lat_lons.append([(G.nodes[node]['y'], G.nodes[node]['x']) for node in route])

        routes_lat_lons.append(route_lat_lons)

    return routes_lat_lons
