import os
import subprocess
import unittest
import shutil

from internal.module.after_effects.domain.usecase.project.export_video_usecase import ExportVideoUseCase
from internal.module.after_effects.domain.usecase.project.open_project_usecase import OpenProjectUseCase
from internal.module.after_effects.domain.value_object.project.export_video_settings import ExportVideoSettings
from internal.module.shared.entity.jsx_entity import JsxEntity


class TestOpenProjectUseCase(unittest.TestCase):
    def setUp(self):
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

        self.project_path = (r'C:\\Users\\Lucas\\PycharmProjects\\python-adobe\\test\\internal\\module\\after_effects\\usecase'
                             r'\\comp\\resources\\test_project.aep')

        self.debug_project_path = os.path.join(self.current_file_path, 'resources/test_project.aep').replace('\\', '\\\\')

        self.usecase = OpenProjectUseCase()

        self.after_effects_path = r'C:\Program Files\Adobe\Adobe After Effects 2023\Support Files\AfterFX.exe'

        self.jsx_entity = JsxEntity("")

    def test_open_project_success(self):
        # arrange

        # act
        result = self.usecase.execute(self.debug_project_path, self.jsx_entity)
        print('path:', self.debug_project_path)
        subprocess.run([self.after_effects_path, '-s', self.jsx_entity.script_file])

        # assert
        self.assertEqual(result, True)

    def test_open_project_failure(self):
        # arrange
        invalid_project_path = "invalid/path"

        # act
        result = self.usecase.execute(invalid_project_path, self.jsx_entity)

        # assert
        self.assertEqual(result, False)
