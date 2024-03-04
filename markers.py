import folium

# Create a map centered around California
california_map = folium.Map(location=[36.7783, -119.4179], zoom_start=6)

# Add markers with popups
locations = [
    {"name": "Los Angeles", "location": [34.0522, -118.2437]},
    {"name": "San Francisco", "location": [37.7749, -122.4194]},
    {"name": "San Diego", "location": [32.7157, -117.1611]}
]

for loc in locations:
    folium.Marker(
        location=loc["location"],
        popup=loc["name"],
        icon=folium.Icon(color='blue')
    ).add_to(california_map)

# Display the map
california_map.save('california_map_with_markers.html')