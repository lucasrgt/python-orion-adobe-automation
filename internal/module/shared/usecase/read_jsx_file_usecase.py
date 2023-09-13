from internal.module.shared.entity.jsx_entity import JsxEntity


class ReadJsxFileUseCase:
    def __init__(self):
        pass

    def execute(self, jsx_entity: JsxEntity) -> bool:
        """Read and convert script file to a format that Python can handle"""

        try:
            with open(jsx_entity.file_path, "r") as file:
                jsx_entity.script_file = file.read().replace("\n", "")
            return True
        except FileNotFoundError as e:
            print(e)
            return False
