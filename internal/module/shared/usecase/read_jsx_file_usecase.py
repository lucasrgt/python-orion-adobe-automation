class ReadJsxFileUseCase:
    def __init__(self):
        pass

    def execute(self, file_path: str) -> str | None:
        """Read and convert script file to a format that Python can handle"""

        try:
            with open(file_path, "r") as file:
                return file.read().replace("\n", "")
        except FileNotFoundError as e:
            print(e)
            return None
