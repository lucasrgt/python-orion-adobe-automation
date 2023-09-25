from abc import ABC, abstractmethod

from internal.module.shared.entity.jsx_entity import JsxEntity


class Controller(ABC):

    @abstractmethod
    def handle(self, data, main_jsx_entity: JsxEntity):
        """
        Handle incoming data and produce an appropriate response.

        :param main_jsx_entity: Main JSX file to be executed.
        :param data: Data to be processed.
        """
        pass
