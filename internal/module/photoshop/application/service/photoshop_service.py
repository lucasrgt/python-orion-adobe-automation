from internal.module.after_effects.application.strategy.change_layer_color_action_strategy import \
    ChangeLayerColorActionStrategy
from internal.module.after_effects.application.strategy.change_layer_image_action_strategy import \
    ChangeLayerImageActionStrategy
from internal.module.after_effects.application.strategy.change_layer_text_strategy import ChangeLayerTextActionStrategy
from internal.module.after_effects.domain.usecase.layer.change_layer_color_usecase import ChangeLayerColorUseCase
from internal.module.after_effects.domain.usecase.layer.change_layer_image_usecase import ChangeLayerImageUseCase
from internal.module.after_effects.domain.usecase.layer.change_layer_text_usecase import ChangeLayerTextUseCase
from internal.module.after_effects.domain.usecase.project.open_project_usecase import OpenProjectUseCase
from internal.module.shared.entity.jsx_entity import JsxEntity


class PhotoshopService:

    def __init__(self,
                 open_project_usecase: OpenProjectUseCase,
                 change_layer_color_usecase: ChangeLayerColorUseCase,
                 change_layer_text_usecase: ChangeLayerTextUseCase,
                 change_layer_image_usecase: ChangeLayerImageUseCase,
                 change_layer_color_action_strategy: ChangeLayerColorActionStrategy,
                 change_layer_text_action_strategy: ChangeLayerTextActionStrategy,
                 change_layer_image_action_strategy: ChangeLayerImageActionStrategy):
        self.open_project_usecase = open_project_usecase
        self.change_layer_color_usecase = change_layer_color_usecase
        self.change_layer_text_usecase = change_layer_text_usecase
        self.change_layer_image_usecase = change_layer_image_usecase
        self.change_layer_color_action_strategy = change_layer_color_action_strategy
        self.change_layer_text_action_strategy = change_layer_text_action_strategy
        self.change_layer_image_action_strategy = change_layer_image_action_strategy

    def process_file(self, file_data):
        jsx_entities = []

        for file in file_data:
            # Open the project
            jsx_entity_project = JsxEntity()
            self.open_project_usecase.execute(jsx_entity_project, file["name"])
            jsx_entities.append(jsx_entity_project)

            # Process the layers
            for layer in file["layers"]:
                layer_name = layer["layerName"]

                # Apply actions to layers
                action_strategies = {
                    "color": self.change_layer_color_action_strategy,
                    "text": self.change_layer_text_action_strategy,
                    "image": self.change_layer_image_action_strategy,
                }

                for action in layer["actions"]:
                    strategy = action_strategies.get(action["type"])
                    if strategy:
                        jsx_entity_action = JsxEntity()
                        strategy.execute(jsx_entity_action, layer_name, action["params"])
                        jsx_entities.append(jsx_entity_action)

        return jsx_entities
