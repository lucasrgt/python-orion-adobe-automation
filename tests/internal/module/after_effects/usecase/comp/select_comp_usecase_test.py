import subprocess
import unittest
import sys
import os

from internal.core.config import project_config
from internal.module.after_effects.domain.usecase.comp.select_comp_usecase import SelectCompUseCase
from internal.module.after_effects.domain.usecase.project.open_project_usecase import OpenProjectUseCase
from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.bundle_jsx_scripts_usecase import BundleJsxScriptsUseCase
from internal.module.shared.usecase.inject_values_into_jsx_usecase import InjectValuesIntoJsxUseCase

current_file_path = os.path.abspath(os.path.dirname(__file__))
src_dir_path = os.path.join(current_file_path, "..", "..", "..", "src")

sys.path.insert(0, src_dir_path)


class MockJsxEntity(JsxEntity):
    pass


class TestSelectCompUseCase(unittest.TestCase):
    def setUp(self):
        # Path Configuration
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

        self.project_path = os.path.join(self.current_file_path, "resources/test_project.aep")

        self.after_effects_path = project_config.AFTER_EFFECTS_PATH

        # Dependencies Setup
        self.main_jsx_entity = MockJsxEntity()
        self.open_project_jsx_entity = MockJsxEntity()
        self.select_comp_jsx_entity = MockJsxEntity()

        inject_values_into_jsx_usecase = InjectValuesIntoJsxUseCase()

        self.bundle_jsx_scripts_usecase = BundleJsxScriptsUseCase()

        self.open_project_usecase = OpenProjectUseCase(inject_values_into_jsx_usecase)

        self.usecase = SelectCompUseCase(inject_values_into_jsx_usecase)

    def test_select_comp_success(self):
        # arrange
        comp_name = "Teste"

        # act
        self.open_project_usecase.execute(self.open_project_jsx_entity, self.project_path)

        result = self.usecase.execute(self.select_comp_jsx_entity, comp_name)

        # bundle it to single execution
        self.bundle_jsx_scripts_usecase.execute(self.main_jsx_entity,
                                                [self.open_project_jsx_entity, self.select_comp_jsx_entity])

        subprocess.run([self.after_effects_path, '-s', self.main_jsx_entity.script_file])

        # assert
        self.assertEqual(result, True)

    def test_select_comp_failure(self):
        # arrange
        invalid_comp_name = "Invalid Comp Name"

        # act
        result = self.usecase.execute(self.jsx_entity, invalid_comp_name)

        # assert
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
