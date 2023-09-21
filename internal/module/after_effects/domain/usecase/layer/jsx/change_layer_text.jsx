if (comp === null) {
  alert('NO COMP HAS BEEN SETUP.');
} else {
  var layerName = '%LAYER_NAME%';
  var newTextContent = '%NEW_TEXT%';

  var textLayer = comp.layer(layerName);

  if (textLayer === null) {
    alert('LAYER NOT FOUND. DOES ' + layerName + ' EXISTS?');
  }

  if (textLayer !== null && textLayer.property('Source Text')) {
    try {
      changeText(textLayer, newTextContent);
    } catch (e) {
      alert('CANNOT CHANGE TEXT:' + e);
    }
  } else {
    alert('NO PROPERTY SOURCE TEXT WAS FOUND IN LAYER ' + layerName);
  }
}

function changeText(textLayer, newText) {
  try {
    var textProp = textLayer.property('Source Text');
    var textDocument = textProp.value;
    textDocument.text = newText;
    textProp.setValue(textDocument);
    alert('Oi');
  } catch (e) {
    alert('CANNOT CHANGE TEXT: ' + e);
  }
}