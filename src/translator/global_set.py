from typing import List
from objects.system import System
from objects.transition import Transition
from objects.template import Model
from objects.variable import Variable

class GlobalSet:
    def __init__(self):
        self.models = []
        self.global_variables = []
        self.sync_transitions = []
        self.system_object = System()

    def get_model_by_name(self, name) -> Model:
        for model in self.models:
            if model.get_model_name() == name:
                return model
        return None

    def get_models(self) -> List[Model]:
        return self.models

    def set_models(self, models : List[Model]):
        self.models = models

    def add_model(self, model : Model):
        self.models.append(model)

    def get_global_variables(self) -> List[Variable]:
        return self.models

    def set_global_variables(self, global_variables : List[Variable]):
        self.global_variables = global_variables

    def add_global_variable(self, global_variable : Variable):
        self.global_variables.append(global_variable)

    def get_sync_transitions(self) -> List[Transition]:
        return self.sync_transitions

    def set_sync_transitions(self, sync_transitions : List[Transition]):
        self.sync_transitions = sync_transitions

    def add_sync_transitions(self, sync_transition : Transition):
        self.sync_transitions.append(sync_transition)

    def get_system_obj(self) -> System:
        return self.system_object

    def get_system_obj(self, system_object : System):
        self.system_object = system_object

    #Call this before get_instance_calls()
    def get_dec_scripts(self):
        script = ""
        declarations = self.system_object.instance_declare
        for declaration in declarations:
            script += declaration + "\n"
        return script

    #Call this after get_instance_delcaration_scripts()
    def get_instance_calls(self):
        script = ""
        calls = self.system_object.instance_call
        for call in calls:
            script += self.system_object.find_templates(call) + "\n"
        return script