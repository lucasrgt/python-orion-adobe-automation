if (comp === null) {
  alert('NO COMP HAS BEEN SETUP.');
} else {
    var layerName = '%LAYER_NAME%';
    var layer = comp.layer(layerName);

    if (layer !== null) {
      var newImagePath = '%IMAGE_PATH%';
      var newFootageItem = app.project.importFile(new ImportOptions(File(newImagePath)));

      if (newFootageItem !== null) {
        layer.replaceSource(newFootageItem, false);
      } else {
        alert('Não foi possível importar a nova imagem.');
      }
    } else {
      alert('Layer não encontrado.');
    }
}
