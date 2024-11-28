import pathlib
from ruamel.yaml import YAML, YAMLError

yaml = YAML()
yaml.explicit_start = True

arguments_path = pathlib.Path.cwd() / "meta" / "argument_specs.yml"
defaults_path = pathlib.Path.cwd() / "defaults" / "main.yml"


def parse_yaml(path):
    data = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.load(f)
    except YAMLError:
        print(f"Failed to parse {path}")
    return data


def make_defaults(arguments):
    data = {k: v["default"] for k, v in arguments["options"].items()}
    with open(defaults_path, "w") as outfile:
        yaml.dump(data, outfile)


if __name__ == "__main__":
    arguments = parse_yaml(arguments_path)
    make_defaults(arguments["argument_specs"]["main"])
