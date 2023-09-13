var file = new File(
    '%PROJECT_PATH%'
);

alert(file);

if (file.exists) {
    app.open(file);
    alert(file.fsName);
    alert('Abriu');
} else {
    alert('File does not exist: ' + file.fsName);
}

alert('Teste');
