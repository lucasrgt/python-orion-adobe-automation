if (comp === null) {
    alert('No comp has been setup.');
} else {
    var layerName = '%LAYER_NAME%';

    var layer = comp.layer(layerName);

    if (layer === null) {
        alert('Layer not found. Does ' + layerName + ' exists?');
    }

    if (layer !== null && layer.effect('Change to Color') != null) {
        try {
            changeColor(1, '%FROM_RGB_COLOR%');
            changeColor(2, '%TO_RGB_COLOR%');
        } catch (e) {
            print('Error:' + e);
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
