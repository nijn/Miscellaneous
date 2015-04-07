Map {
  background-color: transparent;
}

#qtr 
  [zoom >= 14] {
    polygon-fill: rgba(255,255,255, 0);
    line-color: #ccc;
    line-width: .4;
    line-cap: square;
    line-opacity: .3;
    text-name: "[QS]";
    text-face-name: "Roboto Bold";
    text-fill: #AAA;
    text-halo-fill: #EEE;
    text-halo-radius: .25;
    text-size: 12;
  [zoom < 14] {
    polygon-fill: rgba(255,255,255, 0);
    line-width: 0;
  }
}

#sec
  [zoom > 10] {
    polygon-fill: rgba(255,255,255, 0);
    line-color: #ccc;
    line-width: .6;
    line-cap: square;
    line-opacity: .4;
  [zoom > 10][zoom <= 12] {
    text-name: "[SEC]";
    text-face-name: "Arial Bold";
    text-fill: #AAA;
    text-halo-fill: #EEE;
    text-halo-radius: .25;
  }
  [zoom > 12] {
    text-name: "[DESCRIPTOR]";
    text-face-name: "Roboto Bold";
    text-fill: #EFEFEF;
    text-halo-fill: #AAA;
    text-halo-radius: 1;
    text-size: 16;
    text-wrap-character: " ";
    text-wrap-width: 1;
  }
}

#twp {
  polygon-fill: rgba(255,255,255, 0);
  line-color: #ccc;
  line-width: .8;
  line-cap: square;
  line-opacity: .5;
  [zoom < 8] {
    polygon-fill: rgba(255,255,255, 0);
    line-width: 0;
  }
  [zoom > 8][zoom <= 10] {
    text-name: "[DESCRIPTOR]";
    text-face-name: "Roboto Regular";
    text-size: 10;
    text-fill: #777;
    text-halo-fill: #BBB;
    text-halo-radius: .25;
  }
  [zoom > 10][zoom <= 12] {
    text-name: "[DESCRIPTOR]";
    text-face-name: "Roboto Bold";
    text-fill: #EFEFEF;
    text-halo-fill: #AAA;
    text-halo-radius: 1;
    text-size: 19;
  }
}
