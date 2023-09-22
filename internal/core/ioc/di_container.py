# di_container.py
from injector import Injector, singleton, Module, provider

from internal.core.server.module_router import ModuleRouter
from internal.module.after_effects.application.controller.after_effects_controller import AfterEffectsController
from internal.module.after_effects.domain.usecase.comp.select_comp_usecase import SelectCompUseCase
from internal.module.after_effects.domain.usecase.layer.change_layer_color_usecase import ChangeLayerColorUseCase
from internal.module.after_effects.domain.usecase.layer.change_layer_image_usecase import ChangeLayerImageUseCase
from internal.module.after_effects.domain.usecase.layer.change_layer_text_usecase import ChangeLayerTextUseCase
from internal.module.after_effects.domain.usecase.project.export_video_usecase import ExportVideoUseCase
from internal.module.after_effects.domain.usecase.project.open_project_usecase import OpenProjectUseCase
from internal.module.photoshop.application.controller.photoshop_controller import PhotoshopController
from internal.module.shared.usecase.bundle_jsx_scripts_usecase import BundleJsxScriptsUseCase
from internal.module.shared.usecase.inject_values_into_jsx_usecase import InjectValuesIntoJsxUseCase


class DependencyInjectionContainer(Module):

    # Shared Use Cases Injection
    @singleton
    @provider
    def provide_inject_values_into_jsx_usecase(self) -> InjectValuesIntoJsxUseCase:
        return InjectValuesIntoJsxUseCase()

    @singleton
    @provider
    def bundle_jsx_scripts_usecase(self) -> BundleJsxScriptsUseCase:
        return BundleJsxScriptsUseCase()

    # After Effects Use Cases Injection

    @singleton
    @provider
    def provide_open_project_usecase(self,
                                     inject_values_into_jsx_usecase: InjectValuesIntoJsxUseCase) -> OpenProjectUseCase:
        return OpenProjectUseCase(inject_values_into_jsx_usecase)

    @singleton
    @provider
    def provide_export_video_usecase(self) -> ExportVideoUseCase:
        return ExportVideoUseCase()

    @singleton
    @provider
    def provide_select_comp_usecase(self,
                                    inject_values_into_jsx_usecase: InjectValuesIntoJsxUseCase) -> SelectCompUseCase:
        return SelectCompUseCase(inject_values_into_jsx_usecase)

    @singleton
    @provider
    def provide_change_layer_color_usecase(self,
                                           inject_values_into_jsx_usecase: InjectValuesIntoJsxUseCase) -> (
            ChangeLayerColorUseCase):
        return ChangeLayerColorUseCase(inject_values_into_jsx_usecase)

    @singleton
    @provider
    def provide_change_layer_text_usecase(self,
                                          inject_values_into_jsx_usecase: InjectValuesIntoJsxUseCase) -> (
            ChangeLayerTextUseCase):
        return ChangeLayerTextUseCase(inject_values_into_jsx_usecase)

    @singleton
    @provider
    def provide_change_layer_image_usecase(self,
                                           inject_values_into_jsx_usecase: InjectValuesIntoJsxUseCase) -> (
            ChangeLayerImageUseCase):
        return ChangeLayerImageUseCase(inject_values_into_jsx_usecase)

    # Controllers Injection

    @singleton
    @provider
    def provide_after_effects_controller(self) -> AfterEffectsController:
        return AfterEffectsController()

    @singleton
    @provider
    def provide_photoshop_controller(self) -> PhotoshopController:
        return PhotoshopController()

    @singleton
    @provider
    def provide_module_router(self, after_effects_controller: AfterEffectsController,
                              photoshop_controller: PhotoshopController) -> ModuleRouter:
        return ModuleRouter(after_effects_controller, photoshop_controller)


container = Injector(DependencyInjectionContainer)
