var map = L.map('map').setView([36.7783, -119.4179], 6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Function to add custom markers to the map
function addCustomMarkers() {
  var customMarkers = [
    { lat: 37.7749, lon: -122.4194, title: 'San Francisco', color: 'red' },
    { lat: 34.0522, lon: -118.2437, title: 'Los Angeles', color: 'red' },
    // Add more markers as needed
  ];

  customMarkers.forEach(marker => {
    L.circleMarker([marker.lat, marker.lon], {
      color: marker.color,
      fillColor: marker.color,
      fillOpacity: 1,
      radius: 8
    }).bindPopup(marker.title).addTo(map);
  });
}

// Call the function to add custom markers after the map has loaded
map.whenReady(addCustomMarkers);
