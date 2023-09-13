class ExportVideoSettings:
    def __init__(self,
                 aerender_path: str,
                 aep_project_path: str,
                 composition_name: str,
                 output_path: str,
                 output_file_name: str,
                 output_file_format: str):
        self.aerender_path = aerender_path
        self.aep_project_path = aep_project_path
        self.composition_name = composition_name
        self.output_path = output_path
        self.output_file_name = output_file_name
        self.output_file_format = output_file_format

