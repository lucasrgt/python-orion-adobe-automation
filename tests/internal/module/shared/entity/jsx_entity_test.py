import unittest
import sys
import os

from internal.module.shared.entity.jsx_entity import JsxEntity

current_file_path = os.path.abspath(os.path.dirname(__file__))
src_dir_path = os.path.join(current_file_path, "..", "..", "..", "src")

sys.path.insert(0, src_dir_path)


class MockJsxEntity(JsxEntity):
    pass


class TestJsxEntity(unittest.TestCase):
    def setUp(self):
        self.current_file_path = os.path.abspath(os.path.dirname(__file__))

        self.jsx_entity = MockJsxEntity(
            os.path.join(self.current_file_path, "../entity/resource/jsx/test_read.jsx")
        )

    def test_read_success(self):
        # arrange
        expected = "alert('script');"

        # act
        result = self.jsx_entity.read_jsx_file()

        # assert
        self.assertEqual(result, expected)

    def test_read_failure(self):
        # arrange
        jsx_entity_with_invalid_path = MockJsxEntity("./invalid_path/test_read.jsx")

        # act
        result = jsx_entity_with_invalid_path.read_jsx_file()

        # assert
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
