import os

from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.inject_values_into_jsx_usecase import InjectValuesIntoJsxUseCase


class ChangeLayerImageUseCase:
    def __init__(self,
                 inject_values_into_jsx_usecase: InjectValuesIntoJsxUseCase):
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))
        self.inject_values_into_jsx_usecase = inject_values_into_jsx_usecase

    def execute(self,
                jsx_entity: JsxEntity,
                layer_name: str,
                image_path: str):

        # Read the JSX file
        jsx_entity.file_path = os.path.join(self.current_file_path, 'jsx/change_layer_image.jsx')

        ok = jsx_entity.script_file = jsx_entity.read_jsx_file()
        if ok is None:
            return False

        # Inject layer name and text into Change Layer Text script
        sanitized_image_path = image_path.replace('\\', '\\\\')

        replacements = [
            {"template": "%LAYER_NAME%", "value": layer_name},
            {"template": "%IMAGE_PATH%", "value": sanitized_image_path},
        ]

        ok = self.inject_values_into_jsx_usecase.execute(jsx_entity, replacements)
        if ok is False:
            return False

        return True
