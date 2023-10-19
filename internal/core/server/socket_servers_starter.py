import threading
from internal.core.config import project_config
from internal.core.server.base_socket_server import BaseSocketServer
from internal.module.after_effects.application.controller.after_effects_controller import AfterEffectsController
from internal.module.photoshop.application.controller.photoshop_controller import PhotoshopController


class SocketServersStarter:
    def __init__(self,
                 after_effects_controller: AfterEffectsController,
                 photoshop_controller: PhotoshopController):
        self.controllers = {
            'AfterEffects': {'controller': after_effects_controller, 'module_name': "After Effects", 'port': 8001},
            'Photoshop': {'controller': photoshop_controller, 'module_name': "Photoshop", 'port': 8002}
        }

    def start_all(self):
        threads = []
        for name, config in self.controllers.items():
            server = BaseSocketServer(controller=config['controller'], module_name=config['module_name'],
                                      host=project_config.HOST, port=config['port'])
            thread = threading.Thread(target=server.start, name=f"{name}ServerThread")
            threads.append(thread)
            thread.start()

        # Join threads (this will block until all threads are done)
        for thread in threads:
            thread.join()
