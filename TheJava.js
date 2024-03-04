var map = L.map('map').setView([36.7783, -119.4179], 6);
const lats = [37.40124505, 32.8962353, 35.31323904, 35.31323904, 34.441393, 32.776616, 34.06324747, 33.6311555, 37.4083584, 36.18582888, 37.23659905, 32.552662, 34.2015125, 33.65757062, 38.0189574, 34.0044506, 33.941631, 37.77176816, 33.97432, 38.649361, 32.825906, 37.39268995, 34.0328336, 37.7811883, 34.04373, 37.37687135, 37.50965475, 37.41858975, 33.902526, 38.59055615, 37.2944377, 37.7614669, 33.87385945, 38.68455403, 34.0623326, 37.36309473, 37.76683325, 32.80413145, 33.1268426, 37.39776925, 37.6523964, 37.7913454, 38.49172737, 34.0278047, 32.681373, 37.2665722, 37.4216191, 34.179405, 37.3741824]
const longs = [-122.1438405, -117.1960246, -119.0903629, -119.0903629, -119.2585794, -117.0572084, -117.4036484, -117.874638, -121.9540909, -119.3324945, -121.7750134, -116.961837, -118.1729785, -117.7644898, -121.8575416, -117.4939287, -118.424817, -121.9629838, -118.2827719, -121.162846, -117.134327, -122.0470411, -118.4581197, -122.3926454, -118.26014, -121.9228061, -121.9525737, -121.9193582, -118.029115, -121.2786453, -121.9137226, -121.4135088, -118.1621918, -121.7396488, -117.5240655, -121.9401532, -122.4013147, -116.9683146, -117.2670955, -121.8870302, -122.1300114, -122.4032976, -122.407516, -117.9716881, -117.179919, -121.9568188, -122.080368, -118.6015622, -121.9831814, -117.082328]
const company= ["Broadcom Inc.", "Qualcomm Incorporated", "Dryer's Grand Ice Cream", "Dryer's Grand Ice Cream", "Ojai Valley Inn", "Alvarado Hospital, LLC dba Alvarado Hospital Medical Center", "Yellow Corporation", "Tower Semiconductor", "Cisco Systems, Inc.", "Dryer's Grand Ice Cream", "Jabil Inc.", "Ajinomoto Foods North America, Inc.", "California Institute of Technology", "Activision Blizzard", "USS-UPI, LLC", "El Dorado National (California), Inc.", "Federal Express Corporation", "BMO Bank N.A. successor in interest to Bank of the West", "Southern California Pizza Company LLC", "Intel Corporation", "ResMEd Inc.", "LinkedIn Corporation", "Riot Games", "Cruise LLC - Headquarters", "Fashion Institute of Design & Merchandising FIDM", "PayPal", "Jabil Inc.", "Cisco Systems, Inc.", "Shaw Industries Group Inc. Plant WG", "SK hynix NAND Product Solutions Corp. dba Solidigm", "eBay Inc.", "Yellow Corporation", "Matheson Flight Extenders, Inc.", "Woodland Rite Aid Distribution Center", "Yellow Corporation", "TTM Technologies, Inc., subsidiary of TTM Technologies North America, LLC", "Invitae Corporation", "Walmart", "Viasat, Inc", "Becton, Dickinson and Company", "Lonza Biologics, Inc.", "Twitch Interactive, Inc. SFO19 Facility", "Terre du Soleil dba Auberge du Soleil", "Cacique Foods, LLC", "The Hotel del Coronado", "ChargePoint, Inc.", "Surefox North America Inc", "Farmers Group, Inc.", "Qualcomm Incorporated", "Front Porch Communities and Services"]
const layoffs = [1267, 1064, 1015, 1015, 870, 808, 709, 699, 674, 612, 550, 538, 521, 478, 474, 425, 405, 403, 393, 382, 364, 362, 330, 330, 322, 311, 306, 299, 283, 270, 261, 257, 257, 241, 240, 240, 238, 232, 232, 222, 218, 218, 217, 203, 197, 195, 193, 193, 189, 185]
const address = ["3401 Hillview Ave  Palo Alto CA 94304", "5775 Morehouse Drive  San Diego CA 92121", "7901 District Blvd  Bakersfield CA 93313", "7901 District Blvd.  Bakersfield CA 93313", "905 Country Club Road  Ojai CA 93023", "6655 Alvarado Road  San Diego CA 92120", "18298 Slover Avenue  Bloomington CA 92316", "4321 Jamboree Road  Newport Beach CA 92660", "170 West Tasman Drive  San Jose CA 95134", "970 E. Continental  Tulare CA 93274", "30 Great Oaks Boulevard  San Jose CA 95119", "8411 Siempre Viva Rd.  San Diego CA 92154", "4800 Oak Grove Drive  La Canada Flintridge CA 91011", "16215 Alton Pkwy  Irvine CA 92618", "900 Loveridge Road  Pittsburg CA 94565", "9670 Galena St.  JURUPA VALLEY CA 92509", "7401 World Way West  Los Angeles CA 90045", "2527 Camino Ramon  San Ramon CA 94583", "7229 S. Figueroa St.  Los Angeles CA 90003", "1900 Prairie City Rd.  Folsom CA 95630", "9001 Spectrum Center Blvd  San Diego CA 92123", "700 E. Middlefield Road  Mountain View CA 94043", "12333 W Olympic Blvd.  Los Angeles CA 90064", "333 Brannan Street  San Francisco CA 94017", "919 South Grand Avenue  Los Angeles CA 90015", "2211 N. First St.  San Jose CA 95131", "4050 Technology Place  Fremont CA 94538", "560 McCarthy Blvd.  Milpitas CA 95035", "15305 Valley View Drive  Santa Fe Springs CA 90670", "10951 White Rock Rd.  Rancho Cordova CA 95670", "2025 Hamilton Ave  San Jose CA 95125", "1535 E Pescadero Ave.  Tracy CA 95304", "2400 E. Artesia Blvd.  Long Beach CA 90805", "1755 East Beamer Street  Woodland CA 95776", "10661 Etiwanda Ave.  Fontana CA 92337", "407 Mathew Street  Santa Clara CA 95050", "1400 16th Street  San Francisco CA 94103", "605 Fletcher Parkway  El Cajon CA 92020", "6155 El Camino Real  Carlsbad CA 92009", "2350 Qume Drive  San Jose CA 95131", "1978 W. Winton Avenue  Hayward CA 94545", "350 Bush St.  San Francisco CA 94104", "180 Rutherford Hill Road  Rutherford CA 94573", "14940 Proctor Ave  City of Industry CA 91746", "1500 Orange Ave.  Coronado CA 92118", "240 E. Hacienda Avenue  Campbell CA 95008", "2000 North Shoreline Blvd  Mountain View CA 94043", "6301 Owensmouth Avenue  Woodland Hills CA 91367", "3195 Kifer Road  Santa Clara CA 95051", "111 Third Avenue  Chula Vista CA 91910"]

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Function to add custom markers to the map
function addCustomMarkers() {
  var customMarkers = [];
  for (let i = 0; i < lats.length; i++) {
    let compname1 = company[i];
    let info1 = layoffs[i];
    let address1 = address[i];
    customMarkers.push({
      lat: lats,
      lon: longs,
      title: `<body><h>${compname1}</h><p>${info1}</p><p>${address1}</p></body>`,
      color: 'red'
    });
  }

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
