import subprocess

from internal.module.photoshop.application.service.photoshop_service import PhotoshopService
from internal.module.shared.application.interface.controller import Controller
from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.bundle_jsx_scripts_usecase import BundleJsxScriptsUseCase


class PhotoshopController(Controller):
    def __init__(self,
                 main_jsx_entity: JsxEntity,
                 photoshop_service: PhotoshopService,
                 bundle_jsx_scripts_usecase: BundleJsxScriptsUseCase,
                 photoshop_path: str):
        self.main_jsx_entity = main_jsx_entity
        self.photoshop_service = photoshop_service
        self.bundle_jsx_scripts_usecase = bundle_jsx_scripts_usecase
        self.photoshop_path = photoshop_path

    def handle(self, data):
        jsx_entities = self.photoshop_service.process_file(data["files"])

        self.bundle_jsx_scripts_usecase.execute(self.main_jsx_entity, jsx_entities)

        subprocess.run([self.photoshop_path, '-s', self.main_jsx_entity.script_file])
