import os

from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.inject_values_into_jsx_usecase import InjectValuesIntoJsxUseCase
from internal.module.shared.usecase.read_jsx_file_usecase import ReadJsxFileUseCase


class SelectCompUseCase:
    def __init__(self):
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

    def execute(self, comp_name: str):
        select_comp_jsx_entity = JsxEntity(path=os.path.join(self.current_file_path, "./jsx/select_comp.jsx"))

        read_jsx_usecase = ReadJsxFileUseCase()
        ok = read_jsx_usecase.execute(select_comp_jsx_entity)
        if ok is False:
            return False

        replacements = [
            {"template": "%COMPOSITION_NAME%", "value": comp_name},
        ]

        inject_usecase = InjectValuesIntoJsxUseCase()
        ok = inject_usecase.execute(select_comp_jsx_entity, replacements)
        if ok is False:
            return False

        return True
