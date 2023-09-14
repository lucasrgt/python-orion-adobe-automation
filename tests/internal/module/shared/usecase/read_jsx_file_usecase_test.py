import unittest
import sys
import os

from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.read_jsx_file_usecase import ReadJsxFileUseCase

current_file_path = os.path.abspath(os.path.dirname(__file__))
src_dir_path = os.path.join(current_file_path, "..", "..", "..", "src")

sys.path.insert(0, src_dir_path)


class MockJsxEntity(JsxEntity):
    pass


class TestReadJsxFileUseCase(unittest.TestCase):
    def setUp(self):
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

        self.jsx_entity = MockJsxEntity(
            os.path.join(self.current_file_path, "resource/jsx/replace_test.jsx")
        )

        self.usecase = ReadJsxFileUseCase()

    def test_read_success(self):
        # arrange

        # act
        result = self.usecase.execute(self.jsx_entity)

        # assert
        self.assertEqual(result, True)

    def test_read_failure(self):
        # arrange
        jsx_entity_invalid_path = MockJsxEntity("./invalid_path/replace_test.jsx")

        # act
        result = self.usecase.execute(jsx_entity_invalid_path)

        # assert
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
