
from typing import List, Union
from enum import Enum


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

class NLUElement():
    intent: str = None
    slots: List[str] = []


class IntentEnum(Enum):
    capture_app_name = "capture_app_name"
    capture_env_variables = "capture_env_variables"
    capture_framework_name = "capture_framework_name"
    capture_instance_type = "capture_instance_type"
    declare_stages = "declare_stages"

class SlotEnum(Enum):
    pass



def check_conversation_elements(conversation: Conversation) -> Union(bool, str):
    if not conversation.app_name:
        return False, "Needs app_name"
    if not conversation.stages:
        return False, "Needs at least one stage"
    
    for stage in conversation.stages:
        if not stage.name:
            return False, "No name for stage"
        if not stage.jobs:
            return False, f"Needs at least one job for {stage}"
        for job in stage.jobs:
            if not job.name:
                return False, "Needs name for Job"
            if not job.commands:
                return False, "A job needs commands"
            
    return True, "conversation is complete"



def populate_conversation_elements(user_input: NLUElement, conversation: Conversation):
    try:
        intent = IntentEnum(user_input.intent)


    except:
        return conversation
