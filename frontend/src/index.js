import 'ol/ol.css';
import OLCesium from 'olcs/OLCesium';

import {Map as OlMap, View as OlView} from 'ol';
import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer';
import {OSM as OSMSource, XYZ as XYZSource, Vector as VectorSource} from 'ol/source';
import {Style, Fill as StyleFill, Stroke as StyleStroke} from 'ol/style'
import {fromLonLat} from 'ol/proj';
import { Select } from 'ol/interaction'
import {GeoJSON} from 'ol/format'
import Axios from 'axios';
const formatgj = new GeoJSON();
let show3d = false;
let app = document.getElementById('map');
app.style.height = '100vh';
let button = document.getElementById('ganti');

let view = new OlView({
  center: fromLonLat([106.8208828, -6.6169003]),
  zoom: 15,

});

const basemap = new TileLayer({
  source: new XYZSource({
    url: 'http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}'
  })
})
const vl = new VectorLayer({
  source: new VectorSource()
})

const styles = new Style({
  fill: new StyleFill({
    color: '#AAA',
  }),
  stroke: new StyleStroke({
    color: '#F00'
  })
})
vl.setStyle(styles);

let map = new OlMap({
  target: app,
  view: view,
  layers: [basemap, vl],
});
const si = new Select()
map.addInteraction(si);
const ol3d = new OLCesium({map: map});
button.addEventListener('click', function(){
  if (show3d) {
    show3d = false;
  }else{
    show3d = true
  }
  ol3d.setEnabled(show3d);
})

window.ol3d = ol3d;

map.on('click', function(evt){
  const feature = map.forEachFeatureAtPixel(evt.pixel, function(feature){
    return feature
  });

  console.log(feature);
})

async function get_admin(){
  const res = await Axios.get('http://localhost:5000/get_administrasi');
  const result = res.data;
  const response = result.data;
  for (let i = 0; i < response.length; i++) {
    const element = response[i];
    let feature = formatgj.readFeature(element.geojson);
    vl.getSource().addFeature(feature);
    
  }
}

async function get_3d() {
  const res = await Axios.get('http://localhost:5000/get_3d');
  const result = res.data;
  const response = result.data;
  for (let i = 0; i < response.length; i++) {
    const element = response[i];
    let feature = formatgj.readFeature(element.geojson);
    vl.getSource().addFeature(feature);
  }
  
}



// get_admin();
get_3d();

