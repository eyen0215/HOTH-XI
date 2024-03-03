// script.js
var map = L.map('map').setView([36.7783, -119.4179], 6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// You can customize the zoom levels and center coordinates
// based on the region you want to focus on in California.