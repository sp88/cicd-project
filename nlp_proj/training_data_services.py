import os
import json


FILES = [
    'app_name_train_data.json',
    'declare_stages_train_data.json',
    'framework_name_train_data.json'
]


def aggregate_training_data():
    all_train_data = []
    for filename in FILES:
        _filename = f"{os.getcwd()}/nlp_proj/{filename}"
        if os.path.exists(_filename):
            with open(_filename, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                all_train_data.extend(data)
                print(f"{filename} has",len(data))
        else:
            print(f"{filename} does not exist")

    print("all train data len:", len(all_train_data))

    # write to 'train.json'
    all_data_dict = {f"{idx}": data for idx, data in enumerate(all_train_data)}

    f = open(f"{os.getcwd()}/nlp_proj/train.json", "w")
    f.write(json.dumps(all_data_dict, indent=2))
    f.close()


aggregate_training_data()
