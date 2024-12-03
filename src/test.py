import webbrowser

import osmnx as ox
import folium

# Definiere die Koordinaten der Start- und Zielpunkte (Latitude, Longitude)
start_coords = (52.5200, 13.4050)  # Beispiel: Berlin
end_coords = (52.5176, 13.4094)    # Beispiel: Ein anderer Punkt in Berlin

# Lade das Straßennetzwerk der Umgebung
G = ox.graph_from_place("Berlin, Germany", network_type="drive")

# Finde die nächsten Knotenpunkte im Netzwerk für Start- und Zielkoordinaten
start_node = ox.nearest_nodes(G, start_coords[1], start_coords[0])
end_node = ox.nearest_nodes(G, end_coords[1], end_coords[0])

# Berechne die Route zwischen Start- und Endknoten
route = ox.shortest_path(G, start_node, end_node, weight='length')

# Konvertiere die Route in Lat/Lon-Koordinaten
route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]

# Erstelle eine Karte mit dem Startpunkt als Mittelpunkt
m = folium.Map(location=start_coords, zoom_start=14)

# Füge die Route zur Karte hinzu
folium.PolyLine(route_coords, color='blue', weight=5, opacity=0.7).add_to(m)

# Markiere den Start- und Zielpunkt auf der Karte
folium.Marker(start_coords, popup='Start', icon=folium.Icon(color='green')).add_to(m)
folium.Marker(end_coords, popup='Ziel', icon=folium.Icon(color='red')).add_to(m)

# Zeige die Karte an
m.save("test_map.html")
webbrowser.open("test_map.html")
