var file = new File(
    'C:/Users/Lucas/Pictures/ae automation/extendscript/src/scripts/test_project.aep'
);

if (file.exists) {
    app.open(file);
} else {
    alert('File does not exist: ' + file.fsName);
}

alert('Teste');
