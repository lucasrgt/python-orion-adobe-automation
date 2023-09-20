import unittest
import sys
import os

from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.bundle_jsx_scripts_usecase import BundleJsxScriptsUseCase
from internal.module.shared.usecase.read_jsx_file_usecase import ReadJsxFileUseCase

current_file_path = os.path.abspath(os.path.dirname(__file__))
src_dir_path = os.path.join(current_file_path, "..", "..", "..", "src")

sys.path.insert(0, src_dir_path)


class MockJsxEntity(JsxEntity):
    pass


class TestBundleJsxScriptsUseCase(unittest.TestCase):
    def setUp(self):
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

        self.main_jsx_entity = MockJsxEntity(
            os.path.join(self.current_file_path, "resource/jsx/replace_test.jsx")
        )

        self.read_jsx_file_usecase = ReadJsxFileUseCase()

        self.usecase = BundleJsxScriptsUseCase()

        self.jsx_entity_to_bundle_1 = MockJsxEntity(os.path.join(self.current_file_path, "resource/jsx/bundle_test1.jsx"))
        self.jsx_entity_to_bundle_2 = MockJsxEntity(os.path.join(self.current_file_path, "resource/jsx/bundle_test2.jsx"))

    def test_bundle_success(self):
        # arrange
        self.read_jsx_file_usecase.execute(self.jsx_entity_to_bundle_1)
        self.read_jsx_file_usecase.execute(self.jsx_entity_to_bundle_2)

        # act
        self.usecase.execute(self.main_jsx_entity, [self.jsx_entity_to_bundle_1, self.jsx_entity_to_bundle_2])
        result = self.main_jsx_entity.script_file

        # assert
        expected = "alert('juntei');alert('tudo');"
        self.assertEqual(result, expected)

    def test_bundle_failure(self):
        # arrange
        invalid_jsx_entity_to_bundle_1 = MockJsxEntity(os.path.join(self.current_file_path,
                                                                    "./invalid/jsx/bundle_test_invalid.jsx"))

        invalid_jsx_entity_to_bundle_2 = MockJsxEntity(os.path.join(self.current_file_path,
                                                                    "./invalid/jsx/bundle_test_invalid.jsx"))

        self.read_jsx_file_usecase.execute(invalid_jsx_entity_to_bundle_1)
        self.read_jsx_file_usecase.execute(invalid_jsx_entity_to_bundle_2)

        # act
        result = self.usecase.execute(self.main_jsx_entity, [invalid_jsx_entity_to_bundle_1, invalid_jsx_entity_to_bundle_2])

        # assert
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
