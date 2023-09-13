import os

from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.inject_values_into_jsx_usecase import InjectValuesIntoJsxUseCase
from internal.module.shared.usecase.read_jsx_file_usecase import ReadJsxFileUseCase


class OpenProjectUseCase:
    def __init__(self):
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

    def execute(self, project_path: str, jsx_entity: JsxEntity):

        jsx_entity.file_path = os.path.join(self.current_file_path, 'jsx/open_project.jsx')

        read_jsx_usecase = ReadJsxFileUseCase()
        ok = read_jsx_usecase.execute(jsx_entity)
        if ok is False:
            return False

        replacements = [
            {"template": "%PROJECT_PATH%", "value": project_path},
        ]

        inject_usecase = InjectValuesIntoJsxUseCase()
        ok = inject_usecase.execute(jsx_entity, replacements)
        if ok is False:
            return False

        return True
