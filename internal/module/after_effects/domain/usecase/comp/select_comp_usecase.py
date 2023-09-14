import os

from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.inject_values_into_jsx_usecase import InjectValuesIntoJsxUseCase
from internal.module.shared.usecase.read_jsx_file_usecase import ReadJsxFileUseCase


class SelectCompUseCase:
    def __init__(self,
                 read_jsx_file_usecase: ReadJsxFileUseCase,
                 inject_values_into_jsx_usecase: InjectValuesIntoJsxUseCase):
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))
        self.read_jsx_file_usecase = read_jsx_file_usecase
        self.inject_values_into_jsx_usecase = inject_values_into_jsx_usecase

    def execute(self, jsx_entity: JsxEntity, comp_name: str):
        jsx_entity.file_path = os.path.join(self.current_file_path, "jsx/select_comp.jsx")

        # Read the script file
        ok = self.read_jsx_file_usecase.execute(jsx_entity)
        if ok is False:
            return False

        # Inject comp name into Select Comp Script
        replacements = [
            {"template": "%COMPOSITION_NAME%", "value": comp_name},
        ]

        ok = self.inject_values_into_jsx_usecase.execute(jsx_entity, replacements)
        if ok is False:
            return False

        return True
