from typing import List

from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.read_jsx_file_usecase import ReadJsxFileUseCase


class BundleJsxScriptsUseCase:
    def __init__(self):
        pass

    def execute(self, main_jsx_entity: JsxEntity, jsx_entities_to_bundle: List[JsxEntity]) -> bool:
        """Bundle all the jsx files together into one big script,
        so that python subprocess can run all then in AfterEffects/Photoshop/etc.
        without needing to restart it"""

        initial_script = main_jsx_entity.script_file

        try:
            bundled_script = ""

            for jsx_entity in jsx_entities_to_bundle:
                bundled_script += jsx_entity.script_file

            main_jsx_entity.script_file = bundled_script

            if bundled_script == initial_script:
                print("Couldn't bundle the scripts.")
                return False

            return True

        except Exception as e:
            print(e)
            return False
