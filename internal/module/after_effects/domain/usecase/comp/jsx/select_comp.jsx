var compName = '%COMPOSITION_NAME%';

for (var i = 1; i <= app.project.numItems; i++) {
    if (
        app.project.item(i).name === compName &&
        app.project.item(i) instanceof CompItem
    ) {
        comp = app.project.item(i);
        break;
    }
}

if (comp === null) {
    alert('NO COMP FOUND WITH NAME: ' + compName);
}