# Podman-in-Podman Role Template

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border.json)](https://github.com/copier-org/copier)

A template to generate ansible roles with Podman in Podman testing using molecule.

## Usage

### Prerequisite

You will need ``Copier`` to use this template, it is recommended to install it using `pipx <https://pypa.github.io/pipx/installation/>`_.

``` shell
pipx install copier
```

### Basic Usage

Start by generating a blank project

``` shell
copier copy https://github.com/ansible-selfhosted/selfhosted-role-template.git /path/to/project
```

or 

``` shell
copier copy gh:ansible-selfhosted/selfhosted-role-template /path/to/project
```

then you can change directory to your ``/path/to/project`` and initiate your project as
you'd normally do

``` shell
cd /path/to/project
git init
git add .
git commit -m "Initial commit"
```

### Testing

since this project is built around Hatch you will first need it

``` shell
pipx install hatch
```


Then you can run tests using:


``` shell
hatch run test:test
hatch run lint:style
```

### License

This project is licensed under the [MIT License](LICENSE)


⊂(▀¯▀⊂)
