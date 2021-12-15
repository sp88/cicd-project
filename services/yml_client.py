# Regular imports
from copy import deepcopy
from typing import Dict

# Yaml loaders and dumpers
from ruamel.yaml.main import  round_trip_load as yaml_load,  round_trip_dump as yaml_dump

# Yaml commentary
from ruamel.yaml.comments import CommentedMap as OrderedDict, CommentedSeq as OrderedList

# For manual creation of tokens
from ruamel.yaml.tokens import CommentToken
from ruamel.yaml.error import CommentMark

# Globals
# Number of spaces for an indent 
INDENTATION = 2 


# shopping_list = OrderedDict({
#         "eggs": OrderedDict({
#             "type": "free range",
#             "brand": "Mr Tweedy",
#             "amount": 12
#         }),
#         "milk": OrderedDict({
#             "type": "pasteurised",
#             "litres": 1.5,
#             "brands": OrderedList([
#                 "FarmFresh",
#                 "FarmHouse gold",
#                 "Daisy The Cow"
#             ])
#         })
# })
shopping_list = {
    "Shopping List": {
        "eggs": {
            "type": "free range",
            "brand": "Mr Tweedy",
            "amount": 12
        },
        "milk": {
            "type": "pasteurised",
            "litres": 1.5,
            "brands": [
                "FarmFresh",
                "FarmHouse gold",
                "Daisy The Cow"
            ]
        }
    }
}

ci_file = """image: node:7.7.0

cache:
  key: "$CI_PROJECT_ID"
  paths:
    - node_modules/

before_script:
  - npm set progress=false

building:
  stage: build
  variables:
    NODE_ENV: "development"
  script:
    - npm i --no-optional
    - npm run build
  type: build
  tags:
    - npm
    - node
  only:
    - tags
    - master

testing:
  stage: test
  # services:
  #   - mongo:3.2
  #   - rabbitmq:3.6
  #   - redis:3.2
  variables:
    NODE_ENV: "development"
  script:
    - npm i --no-optional
    - npm run test
  type: test
  tags:
    - npm
    - node
  only:
    - tags
    - master

staging:
  stage: deploy
  environment: staging
  variables:
    NODE_ENV: "production"
  script:
    # Run ssh-agent (inside the build environment)
    - eval $(ssh-agent -s)
    # Add the SSH key stored in SSH_RUNNER_KEY variable to the agent store
    - ssh-add <(echo "$SSH_RUNNER_KEY")
    # For Docker builds disable host key checking. Be aware that by adding that
    # you are suspectible to man-in-the-middle attacks.
    - mkdir -p ~/.ssh
    - '[[ -f /.dockerenv ]] && echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config'
    # Install pm2
    - npm i pm2 -g
    # Deploy project
    - pm2 deploy ecosystem.json staging
  type: deploy
  tags:
    - npm
    - node
  only:
    - master"""
# Dump the yaml file
# print(yaml_dump(shopping_list))

f = open("./tmp/.gitlab-ci.yml", "w")
f.write(yaml_dump(ci_file, indent=INDENTATION, block_seq_indent=INDENTATION))
f.close()

def write_yml_file(content: Dict) -> None:
    f = open(".gitlab-ci.yml", "w")
    f.write(yaml_dump(content, indent=INDENTATION, block_seq_indent=INDENTATION))
    f.close()
