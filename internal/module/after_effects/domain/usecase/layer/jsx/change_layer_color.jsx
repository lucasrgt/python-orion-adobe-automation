if (comp === null) {
  alert('NO COMP HAS BEEN SETUP.');
} else {
  var layerName = '%LAYER_NAME%';
  var from_rgb_color = '%FROM_RGB_COLOR%';
  var to_rgb_color = '%TO_RGB_COLOR%';

  var layer = comp.layer(layerName);

  if (layer === null) {
    alert('LAYER NOT FOUND. DOES ' + layerName + ' EXISTS?');
  }

  if (layer !== null && layer.effect('Change to Color') != null) {
    try {
      var from_rgb = eval(from_rgb_color);
      var to_rgb = eval(to_rgb_color);

      convertRgbTo01Scale(from_rgb);
      convertRgbTo01Scale(to_rgb);

      changeColor(1, from_rgb);
      changeColor(2, to_rgb);
    } catch (e) {
      alert('CANNOT CHANGE COLOR:' + e);
    }
  } else {
    alert('NO PROPERTY CHANGE TO COLOR WAS FOUND IN LAYER ' + layerName);
  }
}

function changeColor(effect_param_index, rgb_color) {
  try {
    layer.effect('Change to Color')(effect_param_index).setValue(rgb_color);
  } catch (e) {
    alert('CANNOT CHANGE COLOR: ' + e);
  }
}

function convertRgbTo01Scale(rgb_array) {
  for (var i = 0; i < rgb_array.length; i++) {
    rgb_array[i] = rgb_array[i] / 255.0;
  }
}