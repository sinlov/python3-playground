[![ci](https://github.com/sinlov/python3-playground/actions/workflows/ci.yml/badge.svg)](https://github.com/sinlov/python3-playground/actions/workflows/ci.yml)

[![GitHub license](https://img.shields.io/github/license/sinlov/python3-playground)](https://github.com/sinlov/python3-playground)
[![GitHub latest SemVer tag)](https://img.shields.io/github/v/tag/sinlov/python3-playground)](https://github.com/sinlov/python3-playground/tags)
[![GitHub release)](https://img.shields.io/github/v/release/sinlov/python3-playground)](https://github.com/sinlov/python3-playground/releases)

# this is python3 playground

- repo: [https://github.com/sinlov/python3-playground](https://github.com/sinlov/python3-playground)

## Contributing

[![Contributor Covenant](https://img.shields.io/badge/contributor%20covenant-v1.4-ff69b4.svg)](.github/CONTRIBUTING_DOC/CODE_OF_CONDUCT.md)
[![GitHub contributors](https://img.shields.io/github/contributors/sinlov/python3-playground)](https://github.com/sinlov/python3-playground/graphs/contributors)

We welcome community contributions to this project.

Please read [Contributor Guide](.github/CONTRIBUTING_DOC/CONTRIBUTING.md) for more information on how to get started.

请阅读有关 [贡献者指南](.github/CONTRIBUTING_DOC/zh-CN/CONTRIBUTING.md) 以获取更多如何入门的信息

## env

- run on [python uv](https://docs.astral.sh/uv/) as version `0.9.2`
- now under `pyenv shell 3.11.7`
- style check by [ruff](https://github.com/charliermarsh/ruff)

### Warning

- this project use [gevent](https://www.gevent.org/), but `gevent` [not support windows 10 x64](https://github.com/gevent/gevent/issues/1918)

## dev

```bash
# show help
$ make help

# check env
$ make env

# install dependencies
$ make dep

# run ci pipeline
$ make ci

# fix code style
$ make style

# check style
$ make check
```

## test

### run all test

```bash
$ make test
```

### simple test run

- code at [tests/test_main.py](tests/test_main.py)

```bash
$ uv run python -m unittest tests/test_main.py
```