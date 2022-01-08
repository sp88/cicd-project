
from typing import Dict, List, Union
from enum import Enum

from pydantic import BaseModel


class Command():
    value: str = None

class EnvVariables():
    name: str = None
    value: str = None

class Jobs():
    name: str = None
    commands: List[Command] = []

class Stage():
    name: str = None
    jobs: List[Jobs] = None


class GitInfo():
    repo_name: str = None
    repo_url: str = None
    repo_language: str = None
    repo_framework: str = None
    

class CloudInfo():
    cloud_provider: str = None
    instance_type: str = None
    deployed_url: str = None


class Conversation():
    app_name: str = None
    stages: List[Stage] = []
    env_variables: List[EnvVariables] = None
    git_info: GitInfo = None
    cloud_info: CloudInfo = None


#### Intent/Slot

class NLUElement(BaseModel):
    intent: str = None
    slots: Dict[str, str] = {}


class IntentEnum(Enum):
    capture_app_name = "capture_app_name"
    capture_env_variables = "capture_env_variables"
    capture_framework_name = "capture_framework_name"
    capture_instance_type = "capture_instance_type"
    declare_stages = "declare_stages"

class SlotEnum(Enum):
    env_variables = 'env_variables'
    app_name = 'app_name'
    names_of_stages = 'names_of_stages'
    framework_name = 'framework_name'
    instance_type = 'instance_type'
    cloud_provider = 'cloud_provider'



def prompt_user(conversation: Conversation) -> Union(bool, str):
    if not conversation.app_name:
        return False, "Can you enter application name please?"
    if not conversation.stages:
        return False, "Pipeline needs at least one stage, you declare stages now."
    
    for stage in conversation.stages:
        if not stage.name:
            return False, "No name for stage entered, enter names of stages please."
        if not stage.jobs:
            return False, f"Needs at least one job for {stage}"
        for job in stage.jobs:
            if not job.name:
                return False, f"Needs name for Job, enter name of Job for {stage}"
            if not job.commands:
                return False, f"A job needs commands, please enter any custom commands now for job {job}"
            
    if not conversation.cloud_info.instance_type:
        return False, "What is the instance type that you wish to host the application in?"

    if not conversation.git_info.repo_name:
        return False, "Repository Name neeeded, please enter repository name"

    if not conversation.git_info.repo_framework:
        return False, "Framework name is needed, please enter the Framework you use."

    if not conversation.cloud_info.instance_type:
        return False, "What is the Cloud Instance type need? You can enter values such as 't2.micro'"

    return True, "conversation is complete"



def populate_conversation_elements(user_input: NLUElement, conversation: Conversation):
    try:
        intent = IntentEnum(user_input.intent)
        if not conversation.app_name and user_input.intent == "capture_app_name":
            pass

    except:
        return conversation
