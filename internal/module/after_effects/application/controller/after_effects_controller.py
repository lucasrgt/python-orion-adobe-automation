import subprocess

from internal.module.shared.application.interface.controller import Controller
from internal.module.shared.entity.jsx_entity import JsxEntity


class AfterEffectsController(Controller):
    def __init__(self, after_effects_service, bundle_jsx_scripts_usecase, after_effects_path):
        self.after_effects_service = after_effects_service
        self.bundle_jsx_scripts_usecase = bundle_jsx_scripts_usecase
        self.after_effects_path = after_effects_path

    def handle(self, data, main_jsx_entity: JsxEntity):
        jsx_entities = self.after_effects_service.process_file(data["files"])

        main_jsx_entity = main_jsx_entity
        self.bundle_jsx_scripts_usecase.execute(main_jsx_entity, jsx_entities)

        subprocess.run([self.after_effects_path, '-s', main_jsx_entity.script_file])
