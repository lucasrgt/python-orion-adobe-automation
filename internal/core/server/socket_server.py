import socket
import json

from internal.core.config import project_config
from internal.core.server.module_router import ModuleRouter


def start_socket_server(router: ModuleRouter):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            host = project_config.HOST
            port = project_config.PORT

            s.bind((host, port))
            s.listen()
            print(f"Server listening on {host}:{port}")

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
                        router.route(data)

                    except json.JSONDecodeError:
                        print("Failed to decode JSON. Invalid data received.")
                    except Exception as e:
                        print(f"Error while processing data from {address}: {str(e)}")

    except socket.error as e:
        print(f"Socket error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
