var map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          })
        ],
        view: new ol.View({
          center: ol.proj.fromLonLat([1.4423, 43.6014]),
          zoom: 13
        })
      });

map.on('singleclick', function (event) {
	var coordinate = event.coordinate;
	var coordinate = ol.proj.toLonLat(coordinate);
	var lon = document.getElementById('lon');
	var lat = document.getElementById('lat');
	
	lon.value = coordinate[0];
	lat.value = coordinate[1];
});
