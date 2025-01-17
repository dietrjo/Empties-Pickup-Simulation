import webbrowser
import folium


def create_map(warehouse_location, customer_locations, route_lat_lons):

    tour_map = folium.Map(location=(50.924205555556, 11.586361111111), zoom_start=13, tiles='OpenStreetMap')

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

    tour_map.save('tour_map0.html')

    # Create Tour
    for route_coords in route_lat_lons:
        folium.PolyLine(
            route_coords,
            color="blue",
            weight=3
        ).add_to(tour_map)

    return tour_map
