from typing import Optional


class JsxEntity:
    def __init__(self, file_path: str = "default script file path"):
        self.file_path: str = file_path
        self.script_file: Optional[str] = self.read_jsx_file()

    def read_jsx_file(self) -> Optional[str]:
        """Read and convert script file to a format that Python can handle"""

        if self.file_path == "default script file path":
            return None

        try:
            with open(self.file_path, "r") as file:
                return file.read().replace("\n", "")
        except FileNotFoundError as e:
            print(e)
            return None
