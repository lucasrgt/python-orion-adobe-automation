import os

from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.inject_values_into_jsx_usecase import InjectValuesIntoJsxUseCase


class SelectCompUseCase:
    def __init__(self,
                 inject_values_into_jsx_usecase: InjectValuesIntoJsxUseCase):
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))
        self.inject_values_into_jsx_usecase = inject_values_into_jsx_usecase

    def execute(self, jsx_entity: JsxEntity, comp_name: str):
        # Read the JSX file
        jsx_entity.file_path = os.path.join(self.current_file_path, 'jsx/select_comp.jsx')

        ok = jsx_entity.script_file = jsx_entity.read_jsx_file()
        if ok is None:
            return False

        # Inject comp name into Select Comp Script
        replacements = [
            {"template": "%COMPOSITION_NAME%", "value": comp_name},
        ]

        ok = self.inject_values_into_jsx_usecase.execute(jsx_entity, replacements)
        if ok is False:
            return False

        return True
