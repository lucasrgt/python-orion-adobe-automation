from internal.core.ioc.di_container import container
from internal.core.server.socket_servers_starter import SocketServersStarter


def main():
    try:
        server_starter = container.get(SocketServersStarter)
        server_starter.start_all()

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
