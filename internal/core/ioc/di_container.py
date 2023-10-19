# di_container.py
from typing import Callable

from injector import Injector, singleton, Module, provider

from internal.core.config import project_config
from internal.core.server.socket_servers_starter import SocketServersStarter
from internal.module.after_effects.application.controller.after_effects_controller import AfterEffectsController
from internal.module.after_effects.application.service.after_effects_service import AfterEffectsService
from internal.module.after_effects.application.strategy.change_layer_color_action_strategy import \
    ChangeLayerColorActionStrategy
from internal.module.after_effects.application.strategy.change_layer_image_action_strategy import \
    ChangeLayerImageActionStrategy
from internal.module.after_effects.application.strategy.change_layer_text_strategy import ChangeLayerTextActionStrategy
from internal.module.after_effects.domain.usecase.comp.select_comp_usecase import SelectCompUseCase
from internal.module.after_effects.domain.usecase.layer.change_layer_color_usecase import ChangeLayerColorUseCase
from internal.module.after_effects.domain.usecase.layer.change_layer_image_usecase import ChangeLayerImageUseCase
from internal.module.after_effects.domain.usecase.layer.change_layer_text_usecase import ChangeLayerTextUseCase
from internal.module.after_effects.domain.usecase.project.export_video_usecase import ExportVideoUseCase
from internal.module.after_effects.domain.usecase.project.open_project_usecase import OpenProjectUseCase
from internal.module.photoshop.application.controller.photoshop_controller import PhotoshopController
from internal.module.photoshop.application.service.photoshop_service import PhotoshopService
from internal.module.shared.entity.jsx_entity import JsxEntity
from internal.module.shared.usecase.bundle_jsx_scripts_usecase import BundleJsxScriptsUseCase
from internal.module.shared.usecase.inject_values_into_jsx_usecase import InjectValuesIntoJsxUseCase


class DependencyInjectionContainer(Module):
    # Configuration Injection
    @singleton
    @provider
    def provide_after_effects_path(self) -> str:
        return project_config.AFTER_EFFECTS_PATH

    # Shared Entities Injection
    @provider
    def jsx_entity_factory(self) -> Callable[[], JsxEntity]:
        def create_jsx_entity():
            return JsxEntity()

        return create_jsx_entity

    # Shared Use Cases Injection
    @singleton
    @provider
    def provide_inject_values_into_jsx_usecase(self) -> InjectValuesIntoJsxUseCase:
        return InjectValuesIntoJsxUseCase()

    @singleton
    @provider
    def provide_bundle_jsx_scripts_usecase(self) -> BundleJsxScriptsUseCase:
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

    # Strategies Injection
    @singleton
    @provider
    def provide_change_layer_color_action_strategy(self,
                                                   change_layer_color_usecase: ChangeLayerColorUseCase) -> (
            ChangeLayerColorActionStrategy):
        return ChangeLayerColorActionStrategy(change_layer_color_usecase)

    @singleton
    @provider
    def provide_change_layer_text_action_strategy(self,
                                                  change_layer_text_usecase: ChangeLayerTextUseCase) -> (
            ChangeLayerTextActionStrategy):
        return ChangeLayerTextActionStrategy(change_layer_text_usecase)

    @singleton
    @provider
    def provide_change_layer_image_action_strategy(self,
                                                   change_layer_image_usecase: ChangeLayerImageUseCase) -> (
            ChangeLayerImageActionStrategy):
        return ChangeLayerImageActionStrategy(change_layer_image_usecase)

    # Services Injection
    @singleton
    @provider
    def provide_after_effects_service(self,
                                      open_project_usecase: OpenProjectUseCase,
                                      change_layer_color_usecase: ChangeLayerColorUseCase,
                                      change_layer_text_usecase: ChangeLayerTextUseCase,
                                      change_layer_image_usecase: ChangeLayerImageUseCase,
                                      change_layer_color_action_strategy: ChangeLayerColorActionStrategy,
                                      change_layer_text_action_strategy: ChangeLayerTextActionStrategy,
                                      change_layer_image_action_strategy: ChangeLayerImageActionStrategy) -> (
            AfterEffectsService):
        return AfterEffectsService(open_project_usecase,
                                   change_layer_color_usecase,
                                   change_layer_text_usecase,
                                   change_layer_image_usecase,
                                   change_layer_color_action_strategy,
                                   change_layer_text_action_strategy,
                                   change_layer_image_action_strategy)

    @singleton
    @provider
    def provide_photoshop_service(self,
                                  open_project_usecase: OpenProjectUseCase,
                                  change_layer_color_usecase: ChangeLayerColorUseCase,
                                  change_layer_text_usecase: ChangeLayerTextUseCase,
                                  change_layer_image_usecase: ChangeLayerImageUseCase,
                                  change_layer_color_action_strategy: ChangeLayerColorActionStrategy,
                                  change_layer_text_action_strategy: ChangeLayerTextActionStrategy,
                                  change_layer_image_action_strategy: ChangeLayerImageActionStrategy) -> (
            PhotoshopService):
        return PhotoshopService(open_project_usecase,
                                change_layer_color_usecase,
                                change_layer_text_usecase,
                                change_layer_image_usecase,
                                change_layer_color_action_strategy,
                                change_layer_text_action_strategy,
                                change_layer_image_action_strategy)

    # Controllers Injection
    @singleton
    @provider
    def provide_after_effects_controller(self,
                                         jsx_entity_factory: Callable[[], JsxEntity],
                                         after_effects_service: AfterEffectsService,
                                         bundle_jsx_scripts_usecase: BundleJsxScriptsUseCase,
                                         after_effects_path: str) -> AfterEffectsController:
        main_jsx_entity = jsx_entity_factory()
        return AfterEffectsController(main_jsx_entity,
                                      after_effects_service,
                                      bundle_jsx_scripts_usecase,
                                      after_effects_path)

    @singleton
    @provider
    def provide_photoshop_controller(self,
                                     jsx_entity_factory: Callable[[], JsxEntity],
                                     photoshop_service: PhotoshopService,
                                     bundle_jsx_scripts_usecase: BundleJsxScriptsUseCase,
                                     photoshop_path: str) -> PhotoshopController:
        main_jsx_entity = jsx_entity_factory()
        return PhotoshopController(main_jsx_entity,
                                   photoshop_service,
                                   bundle_jsx_scripts_usecase,
                                   photoshop_path)

    # Server Injection
    @singleton
    @provider
    def provide_socket_servers_starter(self,
                                       after_effects_controller: AfterEffectsController,
                                       photoshop_controller: PhotoshopController) -> SocketServersStarter:
        return SocketServersStarter(after_effects_controller, photoshop_controller)


container = Injector(DependencyInjectionContainer)
