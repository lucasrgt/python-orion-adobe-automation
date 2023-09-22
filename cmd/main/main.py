from internal.core.ioc.di_container import container
from internal.core.server import socket_server
from internal.core.server.module_router import ModuleRouter


def main():
    try:
        module_router = container.get(ModuleRouter)
        socket_server.start_socket_server(module_router)
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
