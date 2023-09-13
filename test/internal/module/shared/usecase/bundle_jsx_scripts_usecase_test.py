import unittest
import sys
import os

from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.bundle_jsx_scripts_usecase import BundleJsxScriptsUseCase

current_file_path = os.path.abspath(os.path.dirname(__file__))
src_dir_path = os.path.join(current_file_path, "..", "..", "..", "src")

sys.path.insert(0, src_dir_path)


class MockJsxEntity(JsxEntity):
    pass


class TestBundleJsxScriptsUseCase(unittest.TestCase):
    def setUp(self):
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

        self.jsx_entity = MockJsxEntity(
            os.path.join(self.current_file_path, "resource/jsx/replace_test.jsx")
        )

        self.usecase = BundleJsxScriptsUseCase()

    def test_bundle_success(self):
        # arrange
        jsx_to_bundle_1 = JsxEntity(os.path.join(self.current_file_path, "resource/jsx/bundle_test1.jsx"))
        jsx_to_bundle_2 = JsxEntity(os.path.join(self.current_file_path, "resource/jsx/bundle_test2.jsx"))

        # act
        self.usecase.execute(self.jsx_entity, [jsx_to_bundle_1, jsx_to_bundle_2])
        result = self.jsx_entity.script_file

        # assert
        expected = "alert('juntei');alert('tudo');"
        self.assertEqual(result, expected)

    def test_bundle_failure(self):
        # arrange
        jsx_to_bundle_1 = JsxEntity(os.path.join(self.current_file_path, "./invalid/jsx/bundle_test_invalid.jsx"))
        jsx_to_bundle_2 = JsxEntity(os.path.join(self.current_file_path, "./invalid/jsx/bundle_test_invalid.jsx"))

        # act
        result = self.usecase.execute(self.jsx_entity, [jsx_to_bundle_1, jsx_to_bundle_2])

        # assert
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
