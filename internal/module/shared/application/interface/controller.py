from abc import ABC, abstractmethod


class Controller(ABC):

    @abstractmethod
    def handle(self, data):
        """
        Handle incoming data and produce an appropriate response.

        :param data: Data to be processed.
        """
        pass
