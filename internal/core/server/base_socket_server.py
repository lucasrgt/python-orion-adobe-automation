import socket
import json

from internal.module.shared.application.interface.controller import Controller


class BaseSocketServer:
    def __init__(self, controller: Controller, module_name: str, host, port):
        self.controller = controller
        self.module_name = module_name
        self.host = host
        self.port = port

    def start(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.host, self.port))
                s.listen()
                print(f"--- {self.module_name} Server ---\n")
                print(f"Server listening on {self.host}:{self.port}\n")

                while True:
                    connection, address = s.accept()
                    print(f"Connection established with: {address}")

                    with connection:
                        try:
                            raw_data = connection.recv(1024)
                            if not raw_data:
                                print("No data received. Closing connection.")
                                break

                            data = json.loads(raw_data)
                            self.controller.handle(data)

                        except json.JSONDecodeError:
                            print("Failed to decode JSON. Invalid data received.")
                        except Exception as e:
                            print(f"Error while processing data from {address}: {str(e)}")

        except socket.error as e:
            print(f"Socket error: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
