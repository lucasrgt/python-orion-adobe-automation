import os
import subprocess

from internal.module.after_effects.domain.value_object.project.export_video_settings import ExportVideoSettings


class ExportVideoUseCase:
    def __init__(self):
        pass

    def execute(self, export_settings: ExportVideoSettings) -> bool:
        full_path = (export_settings.output_path
                     + export_settings.output_file_name
                     + "."
                     + export_settings.output_file_format)

        try:
            cmd = f'"{export_settings.aerender_path}" ' \
                  f'-project "{export_settings.aep_project_path}" ' \
                  f'-output "{full_path}" ' \
                  f'-comp "{export_settings.composition_name}""'

            subprocess.call(cmd, shell=True)

            if not os.path.isfile(full_path):
                return False

            return True

        except Exception as e:
            print(e)
            return False
