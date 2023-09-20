from typing import List, Dict, Any

from internal.module.shared.entity.jsx_entity import JsxEntity


class InjectValuesIntoJsxUseCase:
    def __init__(self):
        pass

    def execute(self,  jsx_entity: JsxEntity, replacements: List[Dict[str, Any]]) -> bool:
        """Inject values to template matcher in the jsx file. E.g: %TEMPLATE% to foo"""

        initial_script = jsx_entity.script_file
        try:
            for replacement in replacements:
                jsx_entity.script_file = jsx_entity.script_file.replace(
                    replacement["template"], replacement["value"]
                )

            if initial_script == jsx_entity.script_file:
                print("Script Template Variable was not found")
                return False

            return True

        except Exception as e:
            print(e)
            return False
