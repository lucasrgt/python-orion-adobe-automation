import os
import subprocess
import unittest

from internal.core.config import project_config
from internal.module.after_effects.domain.usecase.project.open_project_usecase import OpenProjectUseCase
from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.inject_values_into_jsx_usecase import InjectValuesIntoJsxUseCase
from internal.module.shared.usecase.read_jsx_file_usecase import ReadJsxFileUseCase
from tests.helper.jsx_test_helper import JsxTestHelper


class MockJsxEntity(JsxEntity):
    pass


class TestOpenProjectUseCase(unittest.TestCase):
    def setUp(self):
        # Path Configuration
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

        self.project_path = os.path.join(self.current_file_path, 'resources/test_project.aep')

        self.after_effects_path = project_config.after_effects_path

        # Dependencies Setup
        read_jsx_file_usecase = ReadJsxFileUseCase()
        inject_jsx_file_usecase = InjectValuesIntoJsxUseCase()
        self.usecase = OpenProjectUseCase(read_jsx_file_usecase, inject_jsx_file_usecase)

        self.jsx_entity = MockJsxEntity()

    def test_open_project_success(self):
        # arrange

        # act
        result = self.usecase.execute(project_path=self.project_path, jsx_entity=self.jsx_entity)
        subprocess.run([self.after_effects_path, '-s', self.jsx_entity.script_file])

        # assert
        self.assertEqual(result, True)

    def test_open_project_failure(self):
        # arrange
        invalid_project_path = "invalid/path"
        error_img_path = os.path.join(self.current_file_path, 'resources/img_cv/file_does_not_exist.png')

        # act
        self.usecase.execute(project_path=invalid_project_path, jsx_entity=self.jsx_entity)

        process = subprocess.Popen([self.after_effects_path, '-s', self.jsx_entity.script_file])

        result = JsxTestHelper.verify_jsx_script_failure(error_img_path=error_img_path, error_img_confidence=0.7)

        process.wait()

        # assert
        self.assertEqual(result, True)
