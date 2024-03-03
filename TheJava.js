// script.js
var map = L.map('map').setView([36.7783, -119.4179], 6);

L.tileLayer('https://%7Bs%7D.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Add your custom markers
var customMarkers = [
  { lat: 37.7749, lon: -122.4194, title: 'San Francisco', color: 'red' },
  { lat: 34.0522, lon: -118.2437, title: 'Los Angeles', color: 'blue' },
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