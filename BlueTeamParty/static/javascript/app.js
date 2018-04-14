const dataSet = [
[1501427859,37.7,-121.86],
[1468250100,37.04,-121.62],
[1940097339,37.16,-121.65],
[1568919032,37.04,-122.04],
[2040484054,37.39, -122.10]
];

var formatData = function() {
  var output = [];
  dataSet.forEach(dataPoint => {
    var result = { coordinates: [] };
    result.coordinates = [dataPoint[2], dataPoint[1]];
    output.push(result);
  });
  return output;
}

const dataPoints = formatData();
console.log("dataPoints", dataPoints[4].coordinates);

// mapboxgl.accessToken = 'pk.eyJ1Ijoia3NpZGRhbmEiLCJhIjoiY2pmem5ibHg4MHlvMzMzcnFkcDh5Nm9vNiJ9.hbmEp1lSFtee8vgBN97NeQ';
// var map = new mapboxgl.Map({
//   container: 'map',
//   center: [-121.86, 37.7],
//   zoom: 8,
//   style: 'mapbox://styles/mapbox/streets-v10',
//   layer: 'chicago-parks'
// });
//
// const arr = [
//     [-122.1, 37.39],
//     [-121.86, 37.7]
//   ];
//
// const allPoints = arr.map(point => ({
//     type: 'Feature',
//     geometry: {
//         type: 'Point',
//         coordinates: point
//     }
// }));
//
// console.log("allPoints:", allPoints);
//
// map.addLayer({
//     id: 'map',
//     type: 'Point',
//     source: {
//         type: 'geojson',
//         data: {
//             type: 'FeatureCollection',
//             features: allPoints
//         }
//     }
// });


mapboxgl.accessToken = 'pk.eyJ1Ijoia3NpZGRhbmEiLCJhIjoiY2pmem5ibHg4MHlvMzMzcnFkcDh5Nm9vNiJ9.hbmEp1lSFtee8vgBN97NeQ';
var map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/outdoors-v9",
    center: [-121.794385, 37.243331], // -121.794385, 37.243331
    zoom: 9
});

map.on("load", function() {
    map.addSource("national-park", {
        "type": "geojson",
        "data": {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[formatData()]]
                }
            }, {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": dataPoints[0].coordinates,
                }
            }, {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": dataPoints[1].coordinates // 37.16,-121.65
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": dataPoints[2].coordinates // 37.16,-121.65
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": dataPoints[3].coordinates // 37.16,-121.65
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": dataPoints[4].coordinates // 37.16,-121.65
                }
            }]
        }
    });

    map.addLayer({
        "id": "park-boundary",
        "type": "fill",
        "source": "national-park",
        "paint": {
            "fill-color": "#888888",
            "fill-opacity": 0.4
        },
        "filter": ["==", "$type", "Polygon"]
    });

    map.addLayer({
        "id": "park-volcanoes",
        "type": "circle",
        "source": "national-park",
        "paint": {
            "circle-radius": 10,
            "circle-color": "#B42222"
        },
        "filter": ["==", "$type", "Point"],
    });
});

const latlong = { lat: 37.39, lon: -122.10 };

const getWeatherData = (latlong) => {
  fetch('/weather', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
  }, JSON.stringify(latlong))
  .then(response => {
    console.log("response:", response);
    // $("#response-3").text(JSON.stringify(data));
  })
  .catch(error => {
    console.log("error: ", error);
    // $("#response-3").text(JSON.stringify(error));
  })
}
// var formData = {};
// $("form").find("input[name]").each(function (index, node) {
//   formData[node.name] = node.value;
// });
//
// const url = "/weather";
//
// const getWeatherData = (latlong) => {
//   $.post(url, latlong).done(function(data) {
//     console.log("data:", data);
//   });
// }
