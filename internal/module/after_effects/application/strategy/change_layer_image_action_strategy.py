from internal.module.after_effects.domain.usecase.layer.change_layer_image_usecase import ChangeLayerImageUseCase
from internal.module.shared.application.interface.action_strategy import ActionStrategy
from internal.module.shared.entity.jsx_entity import JsxEntity


class ChangeLayerImageActionStrategy(ActionStrategy):
    def __init__(self, change_layer_image_usecase: ChangeLayerImageUseCase):
        self.change_layer_image_usecase = change_layer_image_usecase

    def execute(self, jsx_entity: JsxEntity, layer_name: str, params):
        image_path = params["imagePath"]
        self.change_layer_image_usecase.execute(jsx_entity, layer_name, image_path)
