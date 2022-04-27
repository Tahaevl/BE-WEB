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

var F1 = new ol.Feature({
	geometry: new ol.geom.Point(ol.proj.fromLonLat([1.44228, 43.60142]))
	});

var F2 = new ol.Feature({
	geometry: new ol.geom.Point(ol.proj.fromLonLat([1.45134, 43.59545]))
	});

var F3 = new ol.Feature({
	geometry: new ol.geom.Point(ol.proj.fromLonLat([1.43453, 43.59295]))
	});

var F4 = new ol.Feature({
	geometry: new ol.geom.Point(ol.proj.fromLonLat([1.44773, 43.60463]))
	});

var F5 = new ol.Feature({
	geometry: new ol.geom.Point(ol.proj.fromLonLat([1.43092, 43.59789]))
	});

var style1 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat1jaune.png",
		scale: 0.4
		})
	});

var style2 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat1orange.png",
		scale: 0.4
		})
	});

var style3 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat1rouge.png",
		scale: 0.4
		})
	});

var style4 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat1noir.png",
		scale: 0.4
		})
	});

var style5 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat2jaune.png",
		scale: 0.4
		})
	});

var style6 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat2orange.png",
		scale: 0.4
		})
	});

var style7 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat2rouge.png",
		scale: 0.4
		})
	});

var style8 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat2noir.png",
		scale: 0.4
		})
	});

var style9 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat3jaune.png",
		scale: 0.4
		})
	});

var style10 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat3orange.png",
		scale: 0.4
		})
	});

var style11 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat3rouge.png",
		scale: 0.4
		})
	});

var style12 = new ol.style.Style({
	image: new ol.style.Icon({
		src: "../static/images/cat3noir.png",
		scale: 0.4
		})
	});

var styles = [[style1,style2,style3,style4],[style5,style6,style7,style8],[style9,style10,style11,style12]];

F1.setStyle(styles[2][2]);
F2.setStyle(styles[2][2]);
F3.setStyle(styles[2][2]);
F4.setStyle(styles[2][2]);
F5.setStyle(styles[0][1]);

var markers = [];

var nombre_incidents= donnees.length;

for (let i = 0; i < nombre_incidents; i++) {
	markers.push(new ol.Feature({
		geometry: new ol.geom.Point(ol.proj.fromLonLat([donnees[i][1],donnees[i][2]])),
		name: String(i)
		}));
	}

for (let i = 0; i < nombre_incidents; i++) {
	markers[i].setStyle(styles[donnees[i][9] - 1][donnees[i][5] - 1])
	}

var vector = new ol.layer.Vector({
	source: new ol.source.Vector({
		features: markers
		}),
	name: "Incidents"
	});

map.addLayer(vector);

var container = document.getElementById('popup');
var content = document.getElementById('popup-content');
var closer = document.getElementById('popup-closer');

var overlay = new ol.Overlay({
    element: container,
    autoPan: true,
    autoPanAnimation: {
        duration: 250
    }
});

map.addOverlay(overlay);

var popup2 = document.getElementById('popupDeclarations');
var content2 = document.getElementById('popup-content2');
var closer2 = document.getElementById('popup-closer2');

function openDeclarations() {
	i = parseFloat(content2.innerHTML);
	nombre_declarations = donnees[i][10].length;
	declarations = "<b>Déclarations:</b>";
	for (let k = 0; k < nombre_declarations; k++) {
		declarations = declarations.concat("<br />",donnees[i][10][k][0],": <i>",donnees[i][10][k][1],"</i>");
		}
	content2.innerHTML = declarations;
	console.log(content2.innerHTML);
	popup2.style.display = "block";
	}

closer.onclick = function() {
    overlay.setPosition(undefined);
    closer.blur();
    return false;
};

closer2.onclick = function() {
	popup2.style.display = "none";
	content2.innerHTML = String(i);
};

map.on('singleclick', function (event) {
    if (map.hasFeatureAtPixel(event.pixel) === true) {
        var coordinate = event.coordinate;
        var i = parseFloat(map.getFeaturesAtPixel(event.pixel)[0].getProperties().name);
        content.innerHTML = "<b>".concat(donnees[i][3],": ",donnees[i][4],"</b>",
		"<FONT size='2%'>",
		"<br />Niveau: ",String(donnees[i][5]),
		"<br />Premier signalement: ",String(donnees[i][6]),
		"<br />Dernier signalement: ",String(donnees[i][7]),
		"</FONT>",
		"<br /><i>Description: ",donnees[i][8],"</i>");
	content2.innerHTML = String(i)
	popup2.style.display = "none";

        overlay.setPosition(coordinate);
    } else {
        overlay.setPosition(undefined);
        closer.blur();
    }
});
