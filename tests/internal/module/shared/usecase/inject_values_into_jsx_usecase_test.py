import unittest
import sys
import os

from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.inject_values_into_jsx_usecase import InjectValuesIntoJsxUseCase

current_file_path = os.path.abspath(os.path.dirname(__file__))
src_dir_path = os.path.join(current_file_path, "..", "..", "..", "src")

sys.path.insert(0, src_dir_path)


class MockJsxEntity(JsxEntity):
    pass


class TestInjectValuesIntoJsxUseCase(unittest.TestCase):
    def setUp(self):
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

        self.jsx_entity = MockJsxEntity(
            os.path.join(self.current_file_path, "resource/jsx/replace_test.jsx")
        )

        self.inject_usecase = InjectValuesIntoJsxUseCase()

    def test_inject_success(self):
        # arrange
        replacements = [
            {"template": "%MESSAGE%", "value": "Teste"},
            {"template": "%MESSAGE2%", "value": "#123123"},
        ]

        # act
        result = self.inject_usecase.execute(self.jsx_entity, replacements)

        # assert
        expected = "alert('Teste');alert('#123123');"

        self.assertEqual(result, True)
        self.assertEqual(self.jsx_entity.script_file, expected)

    def test_inject_failure(self):
        # arrange
        invalid_replacements = [
            {"template": "@INVALID@", "value": "Teste"},
            {"template": "@INVALID2@", "value": "#123123"},
        ]

        # act
        result = self.inject_usecase.execute(self.jsx_entity, invalid_replacements)

        # assert
        expected = "alert('%MESSAGE%');alert('%MESSAGE2%');"

        self.assertEqual(result, False)
        self.assertEqual(self.jsx_entity.script_file, expected)


if __name__ == "__main__":
    unittest.main()
