import unittest
import sys
import os

from internal.module.after_effects.domain.usecase.comp.select_comp_usecase import SelectCompUseCase
from internal.module.after_effects.domain.usecase.layer.change_layer_color_usecase import ChangeLayerColorUseCase
from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.inject_values_into_jsx_usecase import InjectValuesIntoJsxUseCase
from internal.module.shared.usecase.read_jsx_file_usecase import ReadJsxFileUseCase

current_file_path = os.path.abspath(os.path.dirname(__file__))
src_dir_path = os.path.join(current_file_path, "..", "..", "..", "src")

sys.path.insert(0, src_dir_path)


class MockJsxEntity(JsxEntity):
    pass


class TestChangeLayerColorUseCase(unittest.TestCase):
    def setUp(self):
        # Path Configuration
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

        self.project_path = os.path.join(self.current_file_path, "resources/test_project.aep")

        # Dependencies Setup
        read_jsx_file_usecase = ReadJsxFileUseCase()
        inject_values_into_jsx_usecase = InjectValuesIntoJsxUseCase()

        self.select_comp_usecase = SelectCompUseCase(read_jsx_file_usecase, inject_values_into_jsx_usecase)
        self.usecase = ChangeLayerColorUseCase(read_jsx_file_usecase, inject_values_into_jsx_usecase)

        self.jsx_entity = JsxEntity()

    def test_select_comp_success(self):
        # arrange
        comp_name = "Teste"
        layer_name = "[TESTE]"
        from_rgb_color = [0, 0, 0]
        to_rgb_color = [100, 150, 200]

        # act
        self.select_comp_usecase.execute(self.jsx_entity, comp_name)
        result = self.usecase.execute(self.jsx_entity, layer_name, from_rgb_color, to_rgb_color)

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
