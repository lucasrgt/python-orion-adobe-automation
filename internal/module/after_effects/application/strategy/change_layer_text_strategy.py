from internal.module.after_effects.domain.usecase.layer.change_layer_text_usecase import ChangeLayerTextUseCase
from internal.module.shared.application.interface.action_strategy import ActionStrategy
from internal.module.shared.entity.jsx_entity import JsxEntity


class ChangeLayerTextActionStrategy(ActionStrategy):
    def __init__(self, change_layer_text_usecase: ChangeLayerTextUseCase):
        self.change_layer_text_usecase = change_layer_text_usecase

    def execute(self, jsx_entity: JsxEntity, layer_name: str, params):
        text = params["textValue"]
        self.change_layer_text_usecase.execute(jsx_entity, layer_name, text)
