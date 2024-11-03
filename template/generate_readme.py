import pathlib
from ruamel.yaml import YAML, YAMLError

yaml = YAML()

meta_path = pathlib.Path(__file__).parent / "meta" / "main.yml"
arguments_path = pathlib.Path(__file__).parent / "meta" / "argument_specs.yml"
extra_data_path = pathlib.Path(__file__).parent / "meta" / "extra_data.yml"
readme_path = pathlib.Path(__file__).parent / "README.md"


def parse_yaml(path):
    data = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.load(f)
    except YAMLError:
        print(f"Failed to parse {path}")
    return data


def make_text(meta, arguments, extras):
    nl = "\n"  # workaround for f-string backslash limitation
    try:
        text = f"""
# Ansible Role: {(
    f"[{meta['galaxy_info']['role_name']}]({extras['related_url']})" 
    if extras['related_url'] 
    else f"{meta['galaxy_info']['role_name']}"
    )}

{meta['galaxy_info']['description']}

## Role Requirements

{(
    "- none" 
    if len(extras['requirements']) == 0 
    else 
    nl.join(f"- {r}" for r in extras['requirements'])
  )}

*Refer to {extras['collection']} collection for general requirements*

## Role Arguments

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
{(
    "".join(f"|{k}|{v['description'][0]}|{v['type']}|{v['required']}|{v['default']}|{nl}" 
    for k, v in arguments['options'].items())
    )}

## Example Playbook

```
- hosts: all
  tasks:
    - name: Importing homepage role
      ansible.builtin.import_role:
        name: selfhosted.{extras['collection']}.{meta['galaxy_info']['role_name']}
      vars:
```

## License

This project is licensed under the [{meta['galaxy_info']['license']} License](LICENSE)


⊂(▀¯▀⊂)

"""
    except KeyError as e:
        raise KeyError(f"key {e} not found, cannot create README.md")

    return text


def inject_to_readme(text, path):
    with open(path, "r") as f:
        lines = f.readlines()
    startline = lines.index("<!-- BEGIN_ANSIBLE_DOCS -->\n")
    endline = lines.index("<!-- END_ANSIBLE_DOCS -->\n")
    new_text = "".join(lines[: startline + 1]) + text + "".join(lines[endline:])
    with open(path, "w") as f:
        f.write(new_text)


if __name__ == "__main__":
    meta = parse_yaml(meta_path)
    arguments = parse_yaml(arguments_path)
    extras = parse_yaml(extra_data_path)
    text = make_text(meta, arguments["argument_specs"]["main"], extras)
    inject_to_readme(text, readme_path)
