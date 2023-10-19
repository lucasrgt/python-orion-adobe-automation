const net = require("net");

const client = net.createConnection({ port: 12777, host: "127.0.0.1" }, () => {
  console.log("Conectado ao servidor Python");

  const dataToSend = {
    module: "after_effects",
    files: [
      {
        name: "test_project.aep",
        layers: [
          {
            layerName: "12345",
            actions: [
              {
                type: "color",
                params: {
                  fromColor: "#ffffff",
                  toColor: "#000000",
                },
              },
              {
                type: "text",
                params: {
                  textValue: "Sample Text",
                },
              },
            ],
          },
          {
            layerName: "67890",
            actions: [
              {
                type: "image",
                params: {
                  imagePath: "path/to/image.jpg",
                },
              },
            ],
          },
        ],
      },
    ],
  };

  client.write(JSON.stringify(dataToSend));
});

client.on("data", (data) => {
  console.log(`Dados recebidos do servidor: ${data}`);
  client.end();
});

client.on("end", () => {
  console.log("Desconectado do servidor");
});
