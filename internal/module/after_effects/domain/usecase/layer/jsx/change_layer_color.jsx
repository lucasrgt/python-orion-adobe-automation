if (comp === null) {
    alert('No comp has been setup.');
} else {
    var layerName = '%LAYER_NAME%';
    var from_rgb_color = '%FROM_RGB_COLOR%';
    var to_rgb_color = '%TO_RGB_COLOR%';

    var layer = comp.layer(layerName);

    if (layer === null) {
        alert('Layer not found. Does ' + layerName + ' exists?');
    }

    if (layer !== null && layer.effect('Change to Color') != null) {
        try {
            var from_rgb = eval(from_rgb_color);
            var to_rgb = eval(to_rgb_color);

            convertRgbTo01ScaleInPlace(from_rgb);
            convertRgbTo01ScaleInPlace(to_rgb);

            alert(from_rgb);
            alert(to_rgb);

            changeColor(1, from_rgb);
            changeColor(2, to_rgb);
        } catch (e) {
            alert('Error:' + e);
        }
        alert('Success.');
    } else {
        alert('No property Change to Color was found in layer ' + layerName);
    }
}

function changeColor(effect_param_index, rgb_color) {
    try {
        layer.effect('Change to Color')(effect_param_index).setValue(rgb_color);
    } catch (e) {
        alert('Error: ' + e);
    }
}

function convertRgbTo01ScaleInPlace(rgb_array) {
    for (var i = 0; i < rgb_array.length; i++) {
        rgb_array[i] = rgb_array[i] / 255.0;
    }
}