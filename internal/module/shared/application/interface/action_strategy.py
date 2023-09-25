from abc import ABC, abstractmethod

from internal.module.shared.entity.jsx_entity import JsxEntity


class ActionStrategy(ABC):

    @abstractmethod
    def execute(self, jsx_entity: JsxEntity, layer_name: str, params):
        pass
