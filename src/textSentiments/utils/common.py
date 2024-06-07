import yaml

def read_yaml(path_to_yaml: str):
    with open(path_to_yaml, 'r') as yaml_file:
        return yaml.safe_load(yaml_file)
