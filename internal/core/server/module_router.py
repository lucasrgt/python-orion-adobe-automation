from internal.module.after_effects.application.controller.after_effects_controller import AfterEffectsController
from internal.module.photoshop.application.controller.photoshop_controller import PhotoshopController


class ModuleRouter:
    def __init__(self, after_effects_controller: AfterEffectsController, photoshop_controller: PhotoshopController):
        self.after_effects_controller = after_effects_controller
        self.photoshop_controller = photoshop_controller

    def route(self, data):
        module_name = data.get('module')

        if module_name == "after_effects":
            self.after_effects_controller.handle_data(data)

        elif module_name == "photoshop":
            self.photoshop_controller.handle_data(data)
