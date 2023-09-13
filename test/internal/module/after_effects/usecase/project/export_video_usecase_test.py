import os
import unittest
import shutil

from internal.module.after_effects.domain.usecase.project.export_video_usecase import ExportVideoUseCase
from internal.module.after_effects.domain.value_object.project.export_video_settings import ExportVideoSettings


class TestExportVideoUseCase(unittest.TestCase):
    def setUp(self):

        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

        self.tmp_folder_path = os.path.join(self.current_file_path, './tmp/')

        if not os.path.exists(self.tmp_folder_path):
            os.mkdir(self.tmp_folder_path)

        self.aerender_path = (
            "C:/Program Files/Adobe/Adobe After Effects 2023/Support Files/aerender.exe"
        )

        self.project_path = os.path.join(self.current_file_path, "resources/test_project.aep")

        self.comp_name = "Teste"

        self.output_path = os.path.join(self.tmp_folder_path)

        self.export_video_usecase = ExportVideoUseCase()

    def tearDown(self):
        if os.path.exists(self.tmp_folder_path):
            shutil.rmtree(self.tmp_folder_path)

        project_log_path = os.path.join(self.current_file_path, "resources/test_project.aep Logs")

        if os.path.exists(project_log_path):
            shutil.rmtree(project_log_path)

    def test_video_export_success(self):
        # arrange
        export_settings = ExportVideoSettings(aerender_path=self.aerender_path,
                                              aep_project_path=self.project_path,
                                              composition_name=self.comp_name,
                                              output_file_name="exported_test_video",
                                              output_file_format="mp4",
                                              output_path=self.tmp_folder_path)

        # act
        result = self.export_video_usecase.execute(export_settings)

        # assert
        self.assertEqual(result, True)

    def test_video_export_failure(self):
        # arrange
        export_settings = ExportVideoSettings(aerender_path=self.aerender_path,
                                              aep_project_path=self.project_path,
                                              composition_name="Invalid Comp",
                                              output_file_name="invalid_video",
                                              output_file_format="mp4",
                                              output_path="./invalid_path")

        # act
        result = self.export_video_usecase.execute(export_settings)

        # assert
        self.assertEqual(result, False)
