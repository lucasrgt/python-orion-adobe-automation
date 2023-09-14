var file = new File(
    '%PROJECT_PATH%'
);

if (file.exists) {
    app.open(file);
} else {
    alert('FILE DOES NOT EXIST: ' + '\n ' + file.fsName);
}