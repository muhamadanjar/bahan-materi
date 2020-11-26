import "ol/ol.css";
import OlMap from "ol/Map";
import OlView from "ol/View";
let app = document.getElementById("map");
let view = new OlView({
  center: [0, 0],
  target: app,
});
let map = new OlMap({
  view: view,
  layers: [],
});
