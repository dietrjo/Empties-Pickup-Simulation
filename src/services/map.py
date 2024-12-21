import folium


def create_map(warehouse_location, customer_locations, routes_lat_lons):

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

    # Create Tours
    tour_colors = ["red", "blue", "yellow", "green"]
    for i in range(len(routes_lat_lons)):
        for route_coords in routes_lat_lons[i]:
            folium.PolyLine(
                route_coords,
                color=tour_colors[i],
                weight=3
            ).add_to(tour_map)

    return tour_map
