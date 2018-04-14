getWeatherData = () => {
  $.ajax({
    url: "/weather",
    type: 'GET',
    success: function(data) {
      return "success";
    },
    error: function(error) {
      $("#response-1").text(JSON.stringify(error));
    }
  });
}


mapboxgl.accessToken = 'pk.eyJ1Ijoia3NpZGRhbmEiLCJhIjoiY2pmem5ibHg4MHlvMzMzcnFkcDh5Nm9vNiJ9.hbmEp1lSFtee8vgBN97NeQ';
var map = new mapboxgl.Map({
  container: 'map',
  center: [-122.1, 37.39],
  zoom: 11.15,
  style: 'mapbox://styles/mapbox/streets-v10'
});
