from internal.module.after_effects.domain.usecase.layer.change_layer_color_usecase import ChangeLayerColorUseCase
from internal.module.shared.application.interface.action_strategy import ActionStrategy
from internal.module.shared.entity.jsx_entity import JsxEntity


class ChangeLayerColorActionStrategy(ActionStrategy):
    def __init__(self, change_layer_color_usecase: ChangeLayerColorUseCase):
        self.change_layer_color_usecase = change_layer_color_usecase

    def execute(self, jsx_entity: JsxEntity, layer_name: str, params):
        from_color = params["fromColor"]
        to_color = params["toColor"]
        self.change_layer_color_usecase.execute(jsx_entity, layer_name, from_color, to_color)
