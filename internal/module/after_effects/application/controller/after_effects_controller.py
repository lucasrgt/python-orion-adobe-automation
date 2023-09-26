import subprocess

from internal.module.after_effects.application.service.after_effects_service import AfterEffectsService
from internal.module.shared.application.interface.controller import Controller
from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.bundle_jsx_scripts_usecase import BundleJsxScriptsUseCase


class AfterEffectsController(Controller):
    def __init__(self,
                 main_jsx_entity: JsxEntity,
                 after_effects_service: AfterEffectsService,
                 bundle_jsx_scripts_usecase: BundleJsxScriptsUseCase,
                 after_effects_path: str):
        self.main_jsx_entity = main_jsx_entity
        self.after_effects_service = after_effects_service
        self.bundle_jsx_scripts_usecase = bundle_jsx_scripts_usecase
        self.after_effects_path = after_effects_path

    def handle(self, data):
        jsx_entities = self.after_effects_service.process_file(data["files"])

        self.bundle_jsx_scripts_usecase.execute(self.main_jsx_entity, jsx_entities)

        subprocess.run([self.after_effects_path, '-s', self.main_jsx_entity.script_file])
