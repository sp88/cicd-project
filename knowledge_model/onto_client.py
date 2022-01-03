from typing import List
from owlready2 import *


onto_path.append(f"{os.getcwd()}/knowledge_model/")

def get_onto():
    return get_ontology("http://test.org/onto.owl")

onto = get_onto()

class Framework(Thing):
    namespace = onto

class DependancyStage(Thing):
    namespace = onto
    windows_commands = List[str]
    linux_commands = List[str]

class TestStage(Thing):
    namespace = onto
    windows_commands = List[str]
    linux_commands = List[str]

class DeployStage(Thing):
    namespace = onto
    windows_commands = List[str]
    linux_commands = List[str]

class has_stages(ObjectProperty):
    namespace = onto
    domain = [Framework]
    range = [DependancyStage, TestStage, DeployStage]

# print(Framework.iri)

flask_framework = Framework("Flask", onto)
flask_dependancy_stage = DependancyStage("Flask Dependancy Stage", onto)
flask_test_stage = TestStage("Flask Test Stage", onto)
flask_deploy_stage = DeployStage("Flask Deploy Stage", onto)
flask_framework.has_stages.append(flask_dependancy_stage)
flask_framework.has_stages.append(flask_test_stage)
flask_framework.has_stages.append(flask_deploy_stage)

# print(flask_framework)
onto.save()

# print(flask_framework.has_stages)
